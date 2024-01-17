import subprocess

def get_current_commit(working_directory: str) -> str:
    try:
        commit_hash = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=working_directory).strip().decode()
        return commit_hash
    except subprocess.CalledProcessError:
        return "Error: Not a git repository, git is not installed, or the specified directory does not exist."
