import requests
import os

def send_notification(job_name, root_cause, fix_applied):
    # Replace with your actual Discord or Slack Webhook URL
    webhook_url = os.getenv("NOTIFIER_WEBHOOK_URL") 
    
    if not webhook_url:
        return

    payload = {
        "username": "Guardian AI",
        "content": "🛡️ **SYSTEM HEALED**",
        "embeds": [{
            "title": f"Pipeline: {job_name}",
            "color": 5763719, # Green
            "fields": [
                {"name": "Detection", "value": root_cause, "inline": False},
                {"name": "Action Taken", "value": f"`{fix_applied}`", "inline": False},
                {"name": "Status", "value": "✅ Verification Build Triggered", "inline": True}
            ],
            "footer": {"text": "Guardian OS • Autonomous SRE"}
        }]
    }
    
    requests.post(webhook_url, json=payload)