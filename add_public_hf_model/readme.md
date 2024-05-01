# Adding Models to `/data/public_models`

This folder contains the code and instructions for adding models to the `/data/public_models` directory on the CAIS cluster. By adding models to this directory, they become accessible to all users on the cluster, saving space and making it easier for others to use them.

## Prerequisites

Before adding a model, make sure you have the following:

- Access to the CAIS cluster
- The repository name of the model you want to add (e.g., `username/model_name`)

## Steps to Add a Model

1. Clone this repository to your local machine or the CAIS cluster.

2. Open the `insert_public_models.py` file and ensure that the `cache_dir` variable points to the correct location of the `/data/public_models` directory on the cluster.

3. Open the `download_models.sh` bash script and add the repository name of the model you want to add to the `models` array. For example:

```bash
models=(
    "username/model_name"
    "another_user/another_model"
)
```

4. Save the changes to both files.

5. Run the download_models.sh script using the following command:

```bash
./download_models.sh
```

This script will submit a job to the Slurm job scheduler for each model in the `models` array. The jobs will download the models from Hugging Face and save them to the `/data/public_models/huggingface` directory.

To perform a dry run without actually submitting the jobs, you can use the --dry flag:
```bash
./download_models.sh --dry
```

6. Once the models are downloaded, they will be available in the /data/public_models/huggingface directory, accessible using the following path:

```bash
/data/public_models/huggingface/{hf_repo}
```

Replace `{hf_repo}` with the repository name of the model.

7. Please set the correct permissions by running the following in the `/data/public_models/huggingface` directory:

```bash
for folder in */; do chmod 777 "$folder"; chmod -R 775 "$folder"*/; done
```

This will ensure that all users have read and execute permissions for the model folders, as well as read/execute/write permissions for the folder that contains the models.

8. Please add the newly added model to the [CAIS Cluster Models spreadsheet](https://docs.google.com/spreadsheets/d/1lF4rx-edniZAon5ExcS8-qa-nLdOxb7tTLHXQ0dLubw/edit#gid=0) so that others can easily find and use it.

Notes:
- The insert_public_models.py script handles the actual downloading of the models from Hugging Face and saving them to the specified directory.
- The download_models.sh script is a bash script that constructs the necessary Slurm job commands and submits them to the job scheduler.
- If you encounter any issues or have questions, please reach out to the CAIS cluster support team or to Richard Ren at hi.richard.ren@gmail.com.

Happy model sharing!