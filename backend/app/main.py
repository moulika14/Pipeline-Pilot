
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from backend.app.services.project_validator import validate_project
from backend.app.services.validation_history import (
    save_validation_report,
    get_validation_history,
)
from backend.app.services.validation_analytics import get_validation_summary


app = FastAPI(
    title="PipelinePilot",
    description="Cloud-Native CI/CD and Deployment Automation Platform",
    version="0.4.0"
)


class ValidationRequest(BaseModel):
    project_path: str


@app.get("/")
def home():
    return {
        "project": "PipelinePilot",
        "status": "running",
        "message": "PipelinePilot backend is ready"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "PipelinePilot API"
    }


@app.post("/validate")
def validate_project_endpoint(request: ValidationRequest):
    report = validate_project(request.project_path)
    saved_report = save_validation_report(report)

    return {
        "validation": report,
        "history_record": saved_report
    }


@app.get("/history")
def history_endpoint():
    history = get_validation_history()

    return {
        "total_reports": len(history),
        "history": history
    }


# Keep this route BEFORE /history/{report_id}
@app.get("/history/summary")
def validation_summary_endpoint():
    return get_validation_summary()


@app.get("/history/{report_id}")
def get_report_by_id(report_id: str):
    history = get_validation_history()

    for record in history:
        if record.get("id") == report_id:
            return record

    raise HTTPException(
        status_code=404,
        detail="Validation report not found"
    )
