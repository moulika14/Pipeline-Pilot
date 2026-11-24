
from backend.app.services.validation_history import get_validation_history


def get_validation_summary() -> dict:
    """Generate analytics from stored validation reports."""

    history = get_validation_history()

    total = len(history)
    passed = 0
    failed = 0

    for record in history:
        report = record.get("report", {})
        status = str(report.get("status", "")).strip().upper()

        if status in ("PASS", "PASSED", "SUCCESS", "SUCCESSFUL"):
            passed += 1
        elif status in ("FAIL", "FAILED", "ERROR"):
            failed += 1

    success_rate = round((passed / total) * 100, 2) if total else 0

    return {
        "total_validations": total,
        "successful_validations": passed,
        "failed_validations": failed,
        "success_rate": success_rate,
        "latest_validation": history[0] if history else None
    }
