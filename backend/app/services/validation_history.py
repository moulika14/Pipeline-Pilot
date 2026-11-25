
import json
from datetime import datetime, timezone
from pathlib import Path
from uuid import uuid4

from sqlalchemy.orm import Session

from backend.app.database.connection import SessionLocal
from backend.app.database.models import ValidationRecord


HISTORY_FILE = (
    Path(__file__).resolve().parent.parent
    / "data"
    / "validation_history.json"
)


def migrate_json_history():
    """Migrate existing JSON records into SQLite."""

    db: Session = SessionLocal()

    try:
        if not HISTORY_FILE.exists():
            return

        existing_records = (
            db.query(ValidationRecord).count()
        )

        if existing_records > 0:
            return

        try:
            history = json.loads(
                HISTORY_FILE.read_text(encoding="utf-8")
            )
        except (json.JSONDecodeError, OSError):
            return

        if not isinstance(history, list):
            return

        for record in history:
            if not isinstance(record, dict):
                continue

            db.add(
                ValidationRecord(
                    id=record.get("id") or str(uuid4()),
                    timestamp=record.get("timestamp")
                    or datetime.now(timezone.utc).isoformat(),
                    report=record.get("report", {})
                )
            )

        db.commit()

    except Exception:
        db.rollback()
        raise

    finally:
        db.close()


def save_validation_report(report: dict) -> dict:
    """Save a validation report to SQLite."""

    db = SessionLocal()

    try:
        record = ValidationRecord(
            id=str(uuid4()),
            timestamp=datetime.now(timezone.utc).isoformat(),
            report=report
        )

        db.add(record)
        db.commit()
        db.refresh(record)

        return {
            "id": record.id,
            "timestamp": record.timestamp,
            "report": record.report
        }

    except Exception:
        db.rollback()
        raise

    finally:
        db.close()


def get_validation_history() -> list:
    """Retrieve validation reports from SQLite."""

    db = SessionLocal()

    try:
        records = (
            db.query(ValidationRecord)
            .order_by(ValidationRecord.timestamp.desc())
            .all()
        )

        return [
            {
                "id": record.id,
                "timestamp": record.timestamp,
                "report": record.report
            }
            for record in records
        ]

    finally:
        db.close()


def get_validation_report_by_id(report_id: str):
    """Retrieve an individual validation report."""

    db = SessionLocal()

    try:
        record = (
            db.query(ValidationRecord)
            .filter(ValidationRecord.id == report_id)
            .first()
        )

        if not record:
            return None

        return {
            "id": record.id,
            "timestamp": record.timestamp,
            "report": record.report
        }

    finally:
        db.close()


def update_validation_report(report_id: str, updated_report: dict):
    """Update an existing validation report."""

    db = SessionLocal()

    try:
        record = (
            db.query(ValidationRecord)
            .filter(ValidationRecord.id == report_id)
            .first()
        )

        if not record:
            return None

        record.report = updated_report
        db.commit()
        db.refresh(record)

        return {
            "id": record.id,
            "timestamp": record.timestamp,
            "report": record.report
        }

    except Exception:
        db.rollback()
        raise

    finally:
        db.close()


def delete_validation_report(report_id: str) -> bool:
    """Delete an existing validation report."""

    db = SessionLocal()

    try:
        record = (
            db.query(ValidationRecord)
            .filter(ValidationRecord.id == report_id)
            .first()
        )

        if not record:
            return False

        db.delete(record)
        db.commit()

        return True

    except Exception:
        db.rollback()
        raise

    finally:
        db.close()
