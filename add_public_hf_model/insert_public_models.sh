#!/bin/bash

# Specify list of models here
models=(
    "01-ai/Yi-34B-Chat"
    "01-ai/Yi-6B-Chat"
    "allenai/OLMo-1B-hf"
    "allenai/OLMo-1.7-7B-hf"
    "allenai/OLMo-7B-SFT"
    "allenai/OLMo-7B-hf"
    "allenai/open-instruct-stanford-alpaca-7b"
)

# Add a command-line argument --dry for dry run

############### SCRIPT BEGINS BELOW ####################

# Implements command-line argument --dry for dry run
DRY_RUN=false
for arg in "$@"; do
    case $arg in
        --dry)
            DRY_RUN=true
            shift
            ;;
    esac
done

# Retrieves username of current user using the whoami command
username=$(whoami)

for model in "${models[@]}"; do
    # Generate job name by replacing slashes with underscores
    job_name="${username}_download_${model//\//\_}"
    
    # Set output path for the job
    output_path="output_2_modelsext/${model//\//\_}.out"
    
    # Construct the command to run using a heredoc
    command_to_run=$(cat <<EOF
#!/bin/bash
#SBATCH --time=24:00:00
#SBATCH --partition=cais
#SBATCH --job-name=$job_name
#SBATCH --output=$output_path
python insert_public_models.py --model_repo=$model
EOF
)
    
    # If dry flag is set, script only prints constructed command but doesn't execute it
    if [ "$DRY_RUN" = "true" ]; then
        echo "$command_to_run"
    else
        # Submit the job to Slurm using sbatch
        echo "$command_to_run" | sbatch
    fi
done