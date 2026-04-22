import subprocess
import os

class Healer:
    def __init__(self):
        
        self.scripts_path = os.path.join(os.path.dirname(__file__), "../../scripts")

    def execute_fix(self, fix_command: str):
        """
        Runs the fix command suggested by AI.
        """
        try:
            print(f"Attempting fix: {fix_command}")
            
            
            result = subprocess.run(
                fix_command, 
                shell=True, 
                capture_output=True, 
                text=True,
                timeout=60 
            )

            if result.returncode == 0:
                return {"status": "success", "output": result.stdout}
            else:
                return {"status": "failed", "error": result.stderr}

        except Exception as e:
            return {"status": "error", "message": str(e)}


if __name__ == "__main__":
    h = Healer()
    print(h.execute_fix("echo 'Testing healer system'"))