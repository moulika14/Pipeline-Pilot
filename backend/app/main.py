from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from backend.app.services.project_validator import validate_project

from backend.app.services.validation_history import (
    migrate_json_history,
    save_validation_report,
    get_validation_history,
    get_validation_report_by_id,
    update_validation_report,
    delete_validation_report,
)

from backend.app.services.validation_analytics import (
    get_validation_summary
)


app = FastAPI(
    title="PipelinePilot",
    description="Cloud-Native CI/CD and Deployment Automation Platform",
    version="0.5.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ValidationRequest(BaseModel):
    project_path: str


class ValidationReportUpdate(BaseModel):
    report: dict


@app.on_event("startup")
def startup_event():
    """Migrate existing validation history on startup."""
    migrate_json_history()


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


# CREATE
@app.post("/validate")
def validate_project_endpoint(request: ValidationRequest):
    report = validate_project(request.project_path)
    saved_report = save_validation_report(report)

    return {
        "validation": report,
        "history_record": saved_report
    }


# READ ALL
@app.get("/history")
def history_endpoint():
    history = get_validation_history()

    return {
        "total_reports": len(history),
        "history": history
    }


# READ SUMMARY
@app.get("/history/summary")
def validation_summary_endpoint():
    return get_validation_summary()


# UPDATE
@app.put("/history/{report_id}")
def update_report_endpoint(
    report_id: str,
    request: ValidationReportUpdate
):
    updated = update_validation_report(
        report_id,
        request.report
    )

    if not updated:
        raise HTTPException(
            status_code=404,
            detail="Validation report not found"
        )

    return {
        "message": "Validation report updated successfully",
        "record": updated
    }


# DELETE
@app.delete("/history/{report_id}")
def delete_report_endpoint(report_id: str):
    deleted = delete_validation_report(report_id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Validation report not found"
        )

    return {
        "message": "Validation report deleted successfully",
        "report_id": report_id
    }


# READ SINGLE
@app.get("/history/{report_id}")
def get_report_by_id(report_id: str):
    record = get_validation_report_by_id(report_id)

    if not record:
        raise HTTPException(
            status_code=404,
            detail="Validation report not found"
        )

    return record
