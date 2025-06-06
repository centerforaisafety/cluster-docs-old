---
layout: post
title: Welcome to the Center for AI Safety Cluster
---

<!-- Alternative ways to do a Table of Contents -->
<!-- # Table of Contents
- toc
{: toc } -->

# Table of Contents  <!-- omit from toc -->
- [Cluster Overview](#cluster-overview)
- [Getting Started](#getting-started)
  - [Getting Cluster Access](#getting-cluster-access)
  - [Getting Help](#getting-help)
  - [Basic Cluster Usage Example](#basic-cluster-usage-example)
    - [Example sbatch file](#example-sbatch-file)
  - [Sharing files and folders with other users](#sharing-files-and-folders-with-other-users)
  - [How to request a shared folder](#how-to-request-a-shared-folder)
  - [Public models and datasets](#public-models-and-datasets)
  - [How to Use the Global Hugging Face Model Cache](#how-to-use-the-global-hugging-face-model-cache)
  - [How to request additional filesystem storage](#how-to-request-additional-filesystem-storage)
- [Package Management](#package-management)
  - [Install Miniconda or Anaconda](#install-miniconda-or-anaconda)
  - [Suggested Installations](#suggested-installations)
- [SLURM Notes](#slurm-notes)
  - [SLURM Example Commands](#slurm-example-commands)
- [Specific Topics](#specific-topics)
  - [Jupyter Notebooks on the Cluster](#jupyter-notebooks-on-the-cluster)
  - [Switching shell such as to ZSH](#switching-shell-such-as-to-zsh)
  - [Installing cmake](#installing-cmake)
  - [Docker Support](#docker-support)
  - [Configuring Notifications](#configuring-notifications)
  - [VS Code on the Cluster](#vs-code-on-the-cluster)
  - [Distributed Training Example](#distributed-training-example)
    - [Basic Example](#basic-example)
    - [Enabling debugging for distributed training](#enabling-debugging-for-distributed-training)

# Cluster Overview

The cluster is hosted on OCI and is based on 32 bare metal BM.GPU.A100-v2.8 nodes and a number of service nodes. Each GPU node is configured with 8 NVIDIA A100 80GB GPU cards, 27.2 TB local NVMe SSD Storage and two 64 core AMD EPYC Milan, for a total of 256 GPUs, 4,096 CPU cores and 870 TB of file system storage.

The nodes are connected by a remote direct memory access (RDMA) network for data communication. Each node has eight 2 x 100 Gbps network interface cards (NICs), providing a total of 1,600 Gbit/sec inter-node network bandwidth with latency as low as single-digit microseconds.

The cluster is run on Ubuntu 22.04 and is managed using Ansible and Terraform. We are in the process of implementing containerization using Singularity. The scheduling system for running jobs on the cluster is SLURM. Storage is managed using the WekaFS Distributed Parallel Filesystem.

SSH fingerprints:
```
256 SHA256:0i6w5GpD9ZEj8l5ozMNoz9bUDdxnyVtGxGb3hgifchE cais-login-0 (ECDSA)
256 SHA256:G7MhKrG1EpE4F/OeI+A8+f33+Avq4n78N3w1rRiRWH4 cais-login-0 (ED25519)
3072 SHA256:OQt+3QcJEYoj53T6JBUIP+Ou3NSY0Qc/SstiNcz4+A0 cais-login-0 (RSA)
```

# Getting Started

## Getting Cluster Access

There is a [form](https://www.safe.ai/compute-cluster) linked on the compute cluster's page on CAIS' website to apply for access.

## Getting Help

To request help, please login to the cluster's Slack workspace and message us in #help-desk channel.  For questions before being granted access please direct them to [compute@safe.ai](mailto:compute@safe.ai). 

## Basic Cluster Usage Example

Once you've given us your ssh key and we've provided your login credentials, you can SSH onto the login node.

```bash
ssh  -i {path-to-private-key} {username}@compute.safe.ai

# Alternatively configure your .ssh/config file to make a nice short version
ssh cais
```

**Important note:** Please do not do any work on the login node. This includes installing things (request a CPU node to do so). 

Test out requesting a node.

```bash
# request 1 cpu on 1 node
srun --pty bash

# Exit from the compute node to request a new node
exit  # or hit Ctrl+d

# On the login node again
# request 2 gpus on 1 node
srun --gpus-per-node=2 --pty bash

# this is more convenient but can fail if you're doing multinode 
# so we suggest the above command  
srun --gpus=2 --pty bash
```

Note for some users you may need to add `--partition=single` before `--pty bash` when requesting a node.

### Example sbatch file

This is a quick example for running jobs non-interactively.  Putting them in the queue.  The suggested workflow is to debug and get things working with srun and then transition into putting jobs into the queue.

This will request 1 gpu on 2 nodes so 2 gpus total. 
It also specifies to run on the interactive partition. 
Feel free to remove that line to have it run on the big partition.

```bash
#!/bin/bash
#SBATCH --nodes=2
#SBATCH --gpus-per-node=1
#SBATCH --time=10:00
#SBATCH --partition=interactive  # OPTIONAL can be removed to run on big/normal partition
#SBATCH --job-name=Example 

# Recommended way if you want to enable gcc version 10 for the "sbatch" session 
source /opt/rh/devtoolset-10/enable

gcc --version  # if you print it out again here it'll be version 10 

python --version  # prints out the python version.  Replace this with a python call to whatever file.

sleep 5
```

## Sharing files and folders with other users

For security measures, if you make your directory readable or executable by other users you will be locked out from `ssh`'ing into the cluster. This prevents other users from manipulating your ssh keys and such.  If you do wish to share we've made the directories `/data/public_models`, `/data/private_models` and `/data/datasets`. Useable by everyone and you can share files and folders there.

## How to request a shared folder

We can set up a folder in the /private_models directory for you to share files with your team. To make it easier to keep track of who is using shared folders in /private_models and be able to remove files that are no longer in use once projects are finished, we are asking everyone that needs to create a new folder to share files with their team to first fill out this brief form: https://airtable.com/appeMGyDPWhtwa3Dw/shr0sUqxVLwokliXW . We will then set up the folder and grant access to the relevant team members. 

This process does not apply to the /public_models folder, which should only be used for models that other teams are likely to want for their research projects.

## Public models and datasets

Many commonly used models (Llama, Mistral, Pythia etc.) can be found in the `/data/public_models` folder, so please check this before downloading them again. Similarly, some popular datasets can be found in the `/data/datasets` folder.


## How to Use the Global Hugging Face Model Cache

The CAIS cluster provides a global Hugging Face model cache to facilitate efficient access to popular resources without affecting your file system quota. This cache is maintained by the CAIS cluster administrators and is regularly updated with frequently used models. Below is a guide on how to utilize this resource.

_**Accessing the Global Cache**_  
The global Hugging Face cache is located at `/data/huggingface/`. You can use the cache by either setting the `cache_dir` argument or by setting the `HF_HOME` environment variable. For example:

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

cache_dir = "/data/huggingface/"
model_name = "meta-llama/Meta-Llama-3-8B-Instruct"

print("Loading model...")
model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto", cache_dir=cache_dir)
tokenizer = AutoTokenizer.from_pretrained(model_name, cache_dir=cache_dir)
```

_**Requesting Models to be Added to the Cache**_  
If you require a model that is not already cached, you can request it by posting in the #shared-models Slack channel. Please include the full name, such as `meta-llama/Meta-Llama-3.1-8B`. Requests are typically processed within 24 hours, subject to approval.

You can view the list of models currently available in the global cache on our [Shared Models Tracker](https://docs.google.com/spreadsheets/d/1q8q1vWuEqaZixtX_XTy0HNIAv8b9zBim_zVRDCLcmfI/edit?gid=0#gid=0).

_**Cache Maintenance and Updates**_  
The global cache is updated regularly, with popular models added automatically. Models that have not been used for over 60 days will be removed.

_**Troubleshooting**_  
Here are some common issues and how to resolve them:  
  - Model Not Found: Double-check the model name for typos. Refer to the Shared Models Tracker for the correct path.  
  - Missing Dependencies: Ensure all required Python packages are installed.
  - Missing Token: Ensure you have an authentication token for models that require them. Consult the Hugging Face documentation for further information.

For additional help, reach out via the #shared-models-data Slack channel.

_**Using Custom Models**_  
If you need to cache a custom model locally, feel free to make use of a local HF cache. However, be mindful of storage quotas and only use local caching when necessary.

## How to request additional filesystem storage

By default, all users of the cluster are limited to 500 GB of file system storage on the cluster. If you need more storage for your project, you can submit an [application](https://airtable.com/appeMGyDPWhtwa3Dw/shrJ5x6XnzqGDx3RV) indicating how much additional storage you need and for how long. We are usually able to provide a decision within 2-3 days.

# Package Management
## Install Miniconda or Anaconda

We suggest installing anaconda or miniconda to facilitate installing many other apps on the server. Here's how we installed miniconda.

```bash
curl https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -o Miniconda3-latest-Linux-x86_64.sh

chmod +x Miniconda3-latest-Linux-x86_64.sh

./Miniconda3-latest-Linux-x86_64.sh
# close and reopen shell or say yes to configure the current shell.
```

Example of how to install [pytorch](https://pytorch.org/get-started/locally/) a popular deep learning library.  Similar commands exist for tensorflow etc.

```
pip3 install torch torchvision torchaudio
```

## Suggested Installations

If you use tmux we recommend installing [tmux-resurrect](https://github.com/tmux-plugins/tmux-resurrect).  This prevents the unfortunate case where if tmux dies so too do all your tabs.  With this app you can resurrect your sessions (if you save them).

# SLURM Notes

The priority of your jobs in the SLURM queue is determined based on the size of the job, the time you've been waiting and your group's previous usage relative to other groups (“fair share”, in SLURM’s terminology).

You should aim to request the minimum number of GPUs needed to run your job efficiently. Requesting more GPUs than needed will result in your group's priority declining faster than otherwise, which means you will need to wait longer in the queue to run jobs in future. You can check the utilisation of GPU cores and memory to see if jobs are running efficiently using:

srun --jobid=<job_id> nvidia-smi

We have configured Slurm for sending email and slack notifications for various job stages (begin, fail, requeue, complete, etc) from the do-not-reply@safe.ai email address (check spam). See the cluster documentation for further details. You can add notifications to your job by adding the following lines to your SBATCH file:
  #SBATCH --mail-user=mailto:{email},slack:{slack-member-id}
  #SBATCH --mail-type=ALL 

Important note: Please do not do any work on the login node. This includes installing things (request a CPU node to do so).

## SLURM Example Commands

```bash
# From the login node
srun --gpus=2 --pty bash  # requests two GPUs to run interactively

# The rest of the commands will work from any node
sbatch launch.sbatch      # Start a job and place it in the queue

scancel #JOB_NUM#         # Pass in the Job number for a specific job to cancel.

scancel --user $USER      # Cancel all jobs that I've started.

sinfo                     # See how many of the nodes are in use.

squeue                    # See where your job is in the queue.


```

# Specific Topics

## Jupyter Notebooks on the Cluster

See Nathaniel Li's [instructions](https://natli.notion.site/IPYNBs-on-CAIS-Compute-Node-ed01ac83448542d6b510847c407766e0) as well.

```bash
# I have configured my .ssh/config so I can do ssh cais_cluster
# If you have not replace cais_cluster with user_name@compute.safe.ai
ssh cais_cluster

# See earlier section about installing anaconda.
# install jupyter notebooks if you haven't already
conda install -c anaconda jupyter
# or use pip to install jupyter notebook

# Get on a compute node
srun  --pty bash

# you'll need to note which compute-permanent-node-## you are on for below.

# Run the following on the compute node
unset XDG_RUNTIME_DIR
export NODEPORT=$(( $RANDOM + 1024 ))
echo $NODEPORT

# You will need the node port so please copy it

jupyter notebook --no-browser --port=$NODEPORT

# You will also need the notebook link that will get printed
# The notebook link will look something like this: 
#  http://localhost:19303/?token=cb2b708e5468268ase8c46448fc28e78bd049a977cdcbd65d1
```

Start a new terminal window

```bash
# Paste the nodeport from above here replacing the #s
export NODEPORT=####

ssh -t -t cais_cluster -L ${NODEPORT}:localhost:${NODEPORT} ssh -N compute-permanent-node-### -L ${NODEPORT}:localhost:${NODEPORT}
```

Finally open up your favorite browser and paste in the link. `http://localhost:19303/?token=cb....`

## Switching shell such as to ZSH

Add the following to the end of your `.bashrc` file which shell you'd like to run.  The different shells are by default installed into `/usr/bin/`

```
# Run zsh
if [ "$SHELL" != "/usr/bin/zsh" ]
then
    export SHELL="/usr/bin/zsh"
    exec /usr/bin/zsh
fi
```

If you're favorite shell is not installed on the system just ask us to add it.

## Installing cmake

`cmake` can be installed via `pip` so we recommend that approach. The `cmake` installed via package manager is old and installing from source will have a more difficult time for upgrades.

```bash
pip install cmake
```

## Docker Support

This is on our roadmap for the coming months.  Please poke us in the Slack if you want this support sooner and we can either reprioritize it or give you our status update on it.

## Configuring Notifications

We have configured SLURM for sending email and Slack notifications for various job stages (begin, fail, requeue, complete, etc) from the `do-not-reply@safe.ai` email address (check spam). It is also capable of interfacing with other notification platforms, so if you would like us to configure it for another platform, let us know and we will look into it. We are using the [goslmailer](https://github.com/CLIP-HPC/goslmailer) for the notifications.

You can add notifications to your job by adding the following lines to your SBATCH file:

```bash
#SBATCH --mail-user=mailto:{email},slack:{slack-member-id}
#SBATCH --mail-type=ALL
```

Feel free to replace `{email}` with one of your choice and `{slack-member-id}` with your personal one for the CAIS Compute Cluster workspace ([how to find your member id](https://www.workast.com/help/article/how-to-find-a-slack-user-id/)). If you would only like to use Slack or email for notifications and not the other, you can do this by only including that service in your sbatch.

Example:

```bash
#SBATCH --mail-user=mailto:{email}
#SBATCH --mail-type=ALL
```

You can also configure the messages with all the [mail-type options](https://slurm.schedmd.com/sbatch.html#OPT_mail-type) found in SLURM by default.  

## VS Code on the Cluster

In our investigations some extensions such as ai autocomplete tools (tabNine and Copilot) have significant cpu utilization. At the moment these are not a problem but we may have to disable these extensions if their usage increases. The main performance impact of VS Code on the cluster is RAM usage, which is nearly entirely decided by the number of extensions installed. This is also impacted by the size of the working directory that you have open in VS Code. Thus we suggest being mindful of how many extensions you install as more than 10 will begin to impact the responsiveness of your connection to the cluster (may vary slightly depending on the extensions).

There are two primary extensions you can use to develop remotely using VS Code. The first, [Remote SSH extension](https://code.visualstudio.com/docs/remote/ssh), can easily be setup for use with the server using the [example ssh setup](#basic-cluster-usage-example). We do require you to change one setting for this extension:
- Go to the extension settings and paste `remote.SSH.remoteServerListenOnSocket` into the search bar at the top. Then make sure the option has a checkmark (disabled by default).

The second option is the [Remote Tunnel extension](https://code.visualstudio.com/docs/remote/tunnels). This extension requires you to ssh into the server in a normal terminal window then run the service manually. It is, however, easier to use on an interactive session of a compute node than Remote SSH and allows you to develop in a browser (and/or the desktop application). We strongly encourage you to run the installation commands from your home directory on the cluster (`/data/yourname`) so the VS Code folders are created with the correct privacy permissions. 

Both of these extensions deliver nearly identical development experiences and differ only in their connection method to the server.

## Distributed Training Example

### Basic Example

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

### Enabling debugging for distributed training

This allows for tracebacks to be recorded.

```python
from torch.distributed.elastic.multiprocessing.errors import record

# Note main should be the main entry point of the code not just a random function. 
# It won't work if your whole code is not in a function for instance.
@record
def main():
    ... # rest of code
```
