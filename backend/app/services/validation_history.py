
import json
from datetime import datetime, timezone
from pathlib import Path
from uuid import uuid4


HISTORY_FILE = (
    Path(__file__).resolve().parent.parent
    / "data"
    / "validation_history.json"
)


def save_validation_report(report: dict) -> dict:
    """Save a validation report to the history file."""

    HISTORY_FILE.parent.mkdir(parents=True, exist_ok=True)

    if HISTORY_FILE.exists():
        try:
            history = json.loads(HISTORY_FILE.read_text(encoding="utf-8"))
            if not isinstance(history, list):
                history = []
        except (json.JSONDecodeError, OSError):
            history = []
    else:
        history = []

    record = {
        "id": str(uuid4()),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "report": report
    }

    history.append(record)

    HISTORY_FILE.write_text(
        json.dumps(history, indent=4),
        encoding="utf-8"
    )

    return record


def get_validation_history() -> list:
    """Retrieve previously saved validation reports."""

    if not HISTORY_FILE.exists():
        return []

    try:
        history = json.loads(HISTORY_FILE.read_text(encoding="utf-8"))
        if isinstance(history, list):
            return list(reversed(history))
        return []
    except (json.JSONDecodeError, OSError):
        return []
