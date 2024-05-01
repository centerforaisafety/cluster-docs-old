from huggingface_hub import HfApi, snapshot_download
import os
import argparse

def download_model(model_repo, cache_dir):
    """
    Download a Hugging Face model and save it to the specified cache directory.

    :param model_repo: The repository name of the model to download.
    :param cache_dir: The directory where the model will be saved.
    :return: The size of the downloaded model in megabytes.
    """
    repo_path = os.path.join(cache_dir, model_repo)
    os.makedirs(repo_path, exist_ok=True)

    snapshot_dir = snapshot_download(
        repo_id=model_repo,
        local_dir=repo_path,
        local_dir_use_symlinks=False,
        # ignore_patterns=["*.msgpack"],  # Exclude unnecessary files
        # allow_patterns=["*.json", "*.py", "*.bin", "*.txt", "*.h5", "*.joblib"],
        local_files_only=False,
    )

    commit_hash = HfApi().repo_info(model_repo).sha
    print(commit_hash)

    # Save the commit hash to a file
    with open(os.path.join(repo_path, "commit_hash.txt"), "w") as file:
        file.write(commit_hash)

    size_bytes = sum(f.stat().st_size for f in os.scandir(repo_path) if f.is_file())
    size_mb = size_bytes / (1024 * 1024)
    return size_mb

def main(model_repo):
    """
    Main function to download a Hugging Face model and calculate the total size of downloaded models.

    :param model_repo: The repository name of the model to download.
    """
    cache_dir = "/data/public_models/huggingface"
    total_size = 0

    print(f"Downloading model: {model_repo}")
    size_mb = download_model(model_repo, cache_dir)
    print(f"Size of {model_repo}: {size_mb:.2f} MB")
    total_size += size_mb

    print(f"Total size of downloaded model: {total_size:.2f} MB")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download a Hugging Face model onto the CAIS cluster.")
    parser.add_argument("--model_repo", type=str, required=True, help="The model repository to download.")
    args = parser.parse_args()
    main(args.model_repo)