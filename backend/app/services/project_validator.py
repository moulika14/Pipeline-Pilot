from pathlib import Path


def validate_project(project_path: str):
    path = Path(project_path)

    if not path.exists() or not path.is_dir():
        return {
            "status": "FAIL",
            "message": "Project directory does not exist or is invalid",
            "project_path": str(path),
            "checks": {},
            "missing_items": ["Valid project directory"],
            "score": "0/6",
            "percentage": 0
        }

    checks = {
        "README.md": (path / "README.md").is_file(),
        "requirements.txt": (path / "requirements.txt").is_file(),
        "Git repository": (path / ".git").exists(),
        "Tests directory": (path / "tests").is_dir(),
        "Main application": (
            (path / "main.py").is_file()
            or (path / "backend" / "app" / "main.py").is_file()
        ),
        "CI workflow": (
            (path / ".github" / "workflows").is_dir()
            and any(
                (path / ".github" / "workflows").glob("*.yml")
            )
            or any(
                (path / ".github" / "workflows").glob("*.yaml")
            )
        )
    }

    missing_items = [
        item for item, passed in checks.items() if not passed
    ]

    passed_checks = sum(checks.values())
    total_checks = len(checks)

    percentage = round((passed_checks / total_checks) * 100)

    if passed_checks == total_checks:
        status = "PASS"
        message = "Project is fully ready for pipeline validation"
    elif passed_checks >= 4:
        status = "WARNING"
        message = "Project is partially ready. Some requirements are missing."
    else:
        status = "FAIL"
        message = "Project needs significant improvements."

    return {
        "status": status,
        "project_path": str(path.resolve()),
        "checks": checks,
        "missing_items": missing_items,
        "score": f"{passed_checks}/{total_checks}",
        "percentage": percentage,
        "message": message
    }