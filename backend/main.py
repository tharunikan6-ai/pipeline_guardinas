import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from services.jenkins_client import JenkinsClient
from agents.analyzer import LogAnalyzer
from agents.healer import Healer
from services.notifier import send_notification
import uvicorn

app = FastAPI(title="Pipeline Guardian API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

jenkins = JenkinsClient()
analyzer = LogAnalyzer()
healer = Healer()

@app.get("/")
def health_check():
    return {"status": "online", "message": "Guardian Brain is active"}

@app.post("/analyze/{job_name}")
async def analyze_pipeline_failure(job_name: str):
    
    logs = jenkins.get_last_build_logs(job_name)
    if "Error" in logs:
        raise HTTPException(status_code=404, detail="Logs not found")

    
    analysis_result = analyzer.analyze(logs)
    
    return {
        "job": job_name,
        "analysis": analysis_result
    }

@app.post("/auto-heal/{job_name}")
async def auto_heal(job_name: str):

    logs = jenkins.get_last_build_logs(job_name)
    if "Error" in logs:
        raise HTTPException(status_code=404, detail="Logs not found")
    
    
    analysis = analyzer.analyze(logs)
    
    
    fix_status = None
    
    confidence = analysis.get("confidence_score", 0)
    
    if confidence > 0.70:
        fix_status = healer.execute_fix(analysis["suggested_fix"])
        
        
        if fix_status.get("status") == "success":
            send_notification(job_name, analysis["root_cause"], analysis["suggested_fix"])
            jenkins.trigger_build(job_name)

    return {
        "job": job_name,
        "analysis": analysis,
        "healing_attempt": fix_status,
        "next_step": "Verification build triggered & Team Notified" if fix_status and fix_status["status"] == "success" else "Manual intervention required"
    }

@app.post("/webhook/jenkins-failure")
async def handle_jenkins_failure(data: dict):
    
    job_name = data.get("job_name")
    
    print(f"🚨 Autopilot Triggered for {job_name}")
    
    return await auto_heal(job_name)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)