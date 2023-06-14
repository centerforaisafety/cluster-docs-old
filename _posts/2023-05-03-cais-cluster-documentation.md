---
layout: post
title: Welcome to the Center for AI Safety Cluster
---

<!-- Alternative ways to do a Table of Contents -->
<!-- # Table of Contents
- toc
{: toc } -->

# Table of Contents
1. [Getting Started](#getting-started)
    1. [Getting Cluster Access](#getting-cluster-access)
    1. [Getting Help](#getting-help)
    1. [Basic Cluster Usage Example](#basic-cluster-usage-example)
    1. [Install Miniconda or Anaconda](#install-miniconda-or-anaconda)
    1. [Suggested Installations](#suggested-installations)
1. [SLURM Notes](#slurm-notes)
    1. [SLURM Example Commands](#slurm-example-commands)
1. [Package Management](#package-management)
    1. [Nix Package Manager](#nix-package-manager)
1. [Specific Topics](#specfic-topics)
    1. [Jupyter Notebooks on the Cluster](#jupyter-notebooks-on-the-cluster)
    1. [Switching shell such as to ZSH](#switching-shell-such-as-to-zsh)
    1. [Installing cmake](#installing-cmake)
    1. [Old GCC, G++, Glibc](#how-to-update-gcc,-g++,-or-glibc)
    1. [Example sbatch file](#example-sbatch-file)
    1. [Docker Support](#docker-support)
    1. [Configuring Notifications](#configuring-notifications)
1. Links to other pages
    1. [Distributed Training Example]({% post_url 2023-04-22-distributed-training-example %})
1. External Resources 
    1. [The SLURM section is similar to how our cluster works](https://rc-docs.northeastern.edu/en/latest/using-discovery/usingslurm.html)

# Getting Started

The Center for AI Safety (CAIS) is launching an initiative to provide free compute support for research projects in ML safety. This is the CAIS Compute Cluster.

- CAIS Compute Cluster is set up for ML safety applications
- 256x A100 GPUs with 80GB memory
- 1,600 Gbit/s inter-node network speeds

## Getting Cluster Access

There is a [short form](https://www.safe.ai/compute-cluster) that one can apply for to gain access to the CAIS Compute Cluster.

## Getting Help

Once granted access please login to slack and message us in #help-desk channel.  For questions before being granted access please direct them to [contact@safe.ai](mailto:contact@safe.ai). 

## Basic Cluster Usage Example

Once you've given us your ssh key and we've set you up. SSH onto the login node.

```bash
ssh  -i {path-to-private-key} {username}@{cluster-login-node-ip}

# Alternatively configure your .ssh/config file to make a nice short version
ssh cais
```

Important note: Please do not do any work on the login node. This includes installing things (request a cpu node to do so).

Test out requesting a node.

```bash
# request 1 cpu on 1 node
srun --pty bash

# Exit from the compute node to request a new node
exit  # or hit Ctrl+d

# On the login node again
# request any 2 gpus available
srun --gpus=2 --pty bash
```

Please note that `--gpus=X` will request X gpus although not necessarily all guaranteed to be on the same node but almost always does assuming you request X < 8.

# Package Management
## Nix Package Manager

Nix is a package manager for Linux and other Unix systems, with a wide selection of up-to-date packages. This document is a brief introduction to Nix and how to use it. 

### How to find packages:
Use `nix-search`, an alias for `nix search nixpkgs#`, to search for packages.

Examples
```bash
# Search for packages with bash function:
$ nix-search hello
```

### How to install packages:
Use `nix-install`, a convienient alias for `nix profile install nixpkgs#`, to install packages.

Examples
```bash
# Install a package(s) with bash function:
$ nix-install hello
$ nix-install hello llvm

# Install a package from a specific branch:
$ nix profile install nixpkgs/release-20.09#hello
```

### How to list installed packages:
Use `nix-list`, an alias for `nix profile list`, to list installed pacakges.

Examples
```bash
# List installed packages with bash function:
$ nix-list
```

### How to remove packages:
Use `nix-list` with `grep` to find a package's id. Use `nix-remove`, an alias for `nix profile remove`, to remove packages.

Examples
```bash
# Remove a specific package by id:
$ nix-list | grep hello
> 1 flake:nixpkgs# ... 2rf7qm44j-hello-2.12.1
# The number at the beginning of the output line above is the package id.

# Use the package id to remove the package
$ nix-remove 1
> removing 'flake:nixpkgs#legacyPackages.aarch64-darwin.hello'
```

### How to upgrade packages:
Use `nix-list` with `grep` to find a package's id. Use `nix-upgrade`, an alias for `nix profile upgrade`, to upgrade packages.

Examples
```bash
# Upgrade all packages that are installed:
$ nix-upgrade '.*'

# Upgrade a specific package by id:
$ nix-list | grep hello
> 1 flake:nixpkgs# ... 2rf7qm44j-hello-2.12.1
# The number at the beginning of the output line above is the package id.

# Use the package id to upgrade the package
$ nix-upgrade 1
```

### Additional Resources:
This tool is powerful and has a lot of functionality that we haven't covered. For more information, about Nix and its value proposition as well as the Nix command, check out the links below.    

[Why Nix?](https://nixos.org/explore.html)  
[Nix command documentation](https://nixos.org/manual/nix/stable/command-ref/experimental-commands.html)


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
conda update conda
conda install pytorch torchvision torchaudio pytorch-cuda=11.7 -c pytorch -c nvidia
```

## Suggested Installations

If you use tmux we recommend installing [tmux-resurrect](https://github.com/tmux-plugins/tmux-resurrect).  This prevents the unfortunate case where if tmux dies so too do all your tabs.  With this app you can resurrect your sessions.

# SLURM Notes

Important note: Please do not do any work on the login node. This includes installing things (request a cpu node to do so).

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

```bash
# I have configured my .ssh/config so I can do ssh cais_cluster
# If you have not replace cais_cluster with user_name@150.230.36.182
ssh cais_cluster

# install jupyter notebooks if you haven't already
conda install -c anaconda jupyter
# or pip install notebook

# Get on a compute node
srun  --pty bash

# you'll need to note which compute-permanent-node-## you are on for below.

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

ssh -t -t cais_cluster -L $NODEPORT:localhost:$NODEPORT ssh -N compute-permanent-node-### -L $NODEPORT:localhost:$NODEPORT
```

Finally open up the browser and paste in the link

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

## How to update gcc, g++, or glibc

If running interactively:

```bash
# The following enables gcc v10 but we also support v6, 8, 10, and 12.
# Simply replace the 10 with one of the other numbers.
scl enable devtoolset-10 bash

# The following enables LLVM.
scl enable llvm-toolset-7.0 bash
```

### Example sbatch file

This will request two gpus on each node so 4 gpus total. 
It also specifies to run on the interactive partition. 
Feel free to remove that line to have it run on the big partition.

```bash
#!/bin/bash
#SBATCH --nodes=2
#SBATCH --gpus-per-node=2
#SBATCH --time=10:00
#SBATCH --partition=interactive  # OPTIONAL can be removed to run on big/normal partition
#SBATCH --job-name=Example 

gcc --version # if you print it out here it'll be 4.8.5  
sleep 5

# Recommended way if you want to enable gcc version 10 for the "sbatch" session 
source /opt/rh/devtoolset-10/enable

gcc --version # if you print it out again here it'll be version 10 

sleep 5
```

## Docker Support

We are actively working on this.  Please poke us in the slack if you want this support sooner and we can either reprioritize it or give you our status update on it.

## Configuring Notifications

We have configured Slurm for sending email and slack notifications for various job stages (begin, fail, requeue, complete, etc) from the `do-not-reply@safe.ai` email address (check spam). It is also capable of interfacing with other notification platforms, so if you would like us to configure it for another platform, let us know and we will look into it. We are using the [goslmailer](https://github.com/CLIP-HPC/goslmailer) for the notifications.

You can add notifications to your job by adding the following lines to your SBATCH file:

```bash
#SBATCH --mail-user=mailto:{email},slack:{slack-member-id}
#SBATCH --mail-type=ALL
```

Feel free to replace `{email}` with one of your choice and `{slack-member-id}` with your personal one for the CAIS Compute Cluster workspace ([how to find your member id](https://www.workast.com/help/article/how-to-find-a-slack-user-id/)). If you would only like to use slack or email for notifications and not the other, you can do this by only including that service in your sbatch.

Example:

```bash
#SBATCH --mail-user=mailto:{email}
#SBATCH --mail-type=ALL
```

You can also configure the messages with all the [mail-type options](https://slurm.schedmd.com/sbatch.html#OPT_mail-type) found in Slurm by default.  