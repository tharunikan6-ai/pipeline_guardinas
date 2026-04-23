import subprocess

class GitService:
    def __init__(self, repo_path="."):
        self.repo_path = repo_path

    def get_last_commit(self):
        return subprocess.check_output(["git", "rev-parse", "HEAD"]).decode().strip()

    def rollback_fix(self):
        """Emergency rollback if the AI fix makes things worse."""
        try:
            subprocess.run(["git", "reset", "--hard", "HEAD~1"], check=True)
            return {"status": "success", "message": "Rollback completed"}
        except Exception as e:
            return {"status": "error", "message": str(e)}