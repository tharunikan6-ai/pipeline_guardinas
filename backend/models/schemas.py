from pydantic import BaseModel, Field
from typing import Optional, List

class AnalysisResult(BaseModel):
    root_cause: str = Field(..., description="The identified reason for failure")
    suggested_fix: str = Field(..., description="The shell command to fix the issue")
    confidence_score: float = Field(default=0.0, ge=0.0, le=1.0)
    severity: str = Field(default="LOW")

class WebhookPayload(BaseModel):
    job_name: str
    build_number: Optional[int] = None
    cause: Optional[str] = "Manual Trigger"

class HealingStatus(BaseModel):
    status: str  
    output: str
    rebuild_triggered: bool