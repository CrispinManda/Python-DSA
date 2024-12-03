import os

def init_repository():
    repo_dir = ".dscs"
    if os.path.exists(repo_dir):
        print("Repository already initialized.")
        return

    # Create .dscs directory and subdirectories
    os.makedirs(os.path.join(repo_dir, "objects"), exist_ok=True)
    os.makedirs(os.path.join(repo_dir, "refs", "heads"), exist_ok=True)

    # Create HEAD file and point to main branch
    with open(os.path.join(repo_dir, "HEAD"), "w") as head_file:
        head_file.write("ref: refs/heads/main\n")

    # Create index file (empty)
    open(os.path.join(repo_dir, "index"), "w").close()

    # Create config file (basic setup)
    with open(os.path.join(repo_dir, "config"), "w") as config_file:
        config_file.write("[core]\nrepositoryformatversion = 0\n")

    print("Initialized empty DSC repository in", os.path.abspath(repo_dir))

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "init":
        init_repository()
    else:
        print("Usage: dscs init")
