import requests
from os import getenv
from dotenv import load_dotenv

load_dotenv()

class JenkinsClient:
    def __init__(self):
        self.url = getenv("JENKINS_URL")
        self.user = getenv("JENKINS_USER")
        self.token = getenv("JENKINS_TOKEN")
        self.auth = (self.user, self.token)

    def get_job_info(self, job_name):
        """Checks if the job exists and returns basic info."""
        response = requests.get(f"{self.url}/job/{job_name}/api/json", auth=self.auth)
        return response.json() if response.status_code == 200 else None

    def get_last_build_logs(self, job_name):
        """Fetches the text logs of the most recent build."""
        log_url = f"{self.url}/job/{job_name}/lastBuild/consoleText"
        response = requests.get(log_url, auth=self.auth)
        if response.status_code == 200:
            return response.text
        return f"Error: Could not fetch logs. Status code: {response.status_code}"

    def trigger_build(self, job_name):
        """Re-runs the pipeline after a fix is applied."""
        trigger_url = f"{self.url}/job/{job_name}/build"
        response = requests.post(trigger_url, auth=self.auth)
        return response.status_code in [200, 201]