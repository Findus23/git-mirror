import subprocess
from pathlib import Path

current_dir = Path(__file__).parent

repo_dir = current_dir / "repos"

source_remote_name = "origin"
target_remote_name = "target"

for dir in repo_dir.glob("*"):
    print(dir)
    print("pull")
    subprocess.run(["git", "remote", "update", source_remote_name], check=True, cwd=dir)
    print("push")
    subprocess.run(["git", "push", target_remote_name], check=True, cwd=dir)
    # --mirror is implicit due to remote config
