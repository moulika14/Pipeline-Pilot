from pathlib import Path


def validate_project(project_path: str):
    path = Path(project_path)

    if not path.exists() or not path.is_dir():
        return {
            "status": "FAIL",
            "message": "Project directory does not exist",
            "project_path": str(path),
            "checks": {},
            "missing_items": ["Valid project directory"],
            "score": 0
        }

    checks = {
        "README.md": (path / "README.md").is_file(),
        "requirements.txt": (path / "requirements.txt").is_file(),
        "Git repository": (path / ".git").exists(),
        "Tests directory": (path / "tests").is_dir()
    }

    missing_items = [
        item for item, passed in checks.items() if not passed
    ]

    score = sum(checks.values())

    status = "PASS" if score == len(checks) else "FAIL"

    return {
        "status": status,
        "project_path": str(path.resolve()),
        "checks": checks,
        "missing_items": missing_items,
        "score": f"{score}/{len(checks)}",
        "message": (
            "Project is ready for pipeline validation"
            if status == "PASS"
            else "Project needs attention before pipeline validation"
        )
    } 