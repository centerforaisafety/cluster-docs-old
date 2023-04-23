---
layout: post
title: Distributed Training Example
---

The following requires pytorch 2.0.  The example though is meant to be simple enough to be a starting point.

The following file is the `launch.sbatch`. You run it with `sbatch launch.sbatch`.

```bash
#!/bin/bash
#SBATCH --nodes 2
#SBATCH --gpus-per-node=8
#SBATCH --job-name dist_gpu
#SBATCH --partition interactive

export MASTER_ADDR=$(scontrol show hostname ${SLURM_NODELIST} | head -n 1)

echo $MASTER_ADDR

srun torchrun --nnodes=2 --nproc_per_node=8 --rdzv_id=100 --rdzv_backend=c10d --rdzv_endpoint=$MASTER_ADDR:29400 dist_training.py
```

The above file will call the python file below that we named `dist_training.py`.  You can see the name at the end of the `srun` command.

```python
import torch
import torch.distributed as dist
import torch.nn as nn
import torch.optim as optim

from torch.nn.parallel import DistributedDataParallel as DDP

class ToyModel(nn.Module):
    def __init__(self):
        super(ToyModel, self).__init__()
        self.net1 = nn.Linear(10, 10)
        self.relu = nn.ReLU()
        self.net2 = nn.Linear(10, 5)

    def forward(self, x):
        return self.net2(self.relu(self.net1(x)))


def demo_basic():
    dist.init_process_group("nccl")
    rank = dist.get_rank()
    print(f"Start running basic DDP example on rank {rank}.")

    # create model and move it to GPU with id rank
    device_id = rank % torch.cuda.device_count()
    model = ToyModel().to(device_id)
    ddp_model = DDP(model, device_ids=[device_id])
    print(f"Moving model to GPUs.")


    loss_fn = nn.MSELoss()
    optimizer = optim.SGD(ddp_model.parameters(), lr=0.001)

    optimizer.zero_grad()
    outputs = ddp_model(torch.randn(20, 10))
    labels = torch.randn(20, 5).to(device_id)
    loss_fn(outputs, labels).backward()
    optimizer.step()
    print(f"Took a gradient step.")
    print(f"Done.")

if __name__ == "__main__":
    demo_basic()
```
