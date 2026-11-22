from pathlib import Path
from backend.app.services.project_validator import validate_project


def create_valid_project(tmp_path):
    (tmp_path / "README.md").write_text("# Test Project")
    (tmp_path / "requirements.txt").write_text("fastapi")
    (tmp_path / ".git").mkdir()
    (tmp_path / "tests").mkdir()

    # Main application
    (tmp_path / "main.py").write_text("print('Application started')")

    # CI workflow
    workflows = tmp_path / ".github" / "workflows"
    workflows.mkdir(parents=True)
    (workflows / "ci.yml").write_text("name: CI\n")


def test_valid_project(tmp_path):
    create_valid_project(tmp_path)

    result = validate_project(str(tmp_path))

    assert result["status"] == "PASS"
    assert result["score"] == "6/6"
    assert result["percentage"] == 100
    assert result["missing_items"] == []


def test_missing_files(tmp_path):
    (tmp_path / ".git").mkdir()
    (tmp_path / "tests").mkdir()

    result = validate_project(str(tmp_path))

    assert result["status"] == "FAIL"
    assert "README.md" in result["missing_items"]
    assert "requirements.txt" in result["missing_items"]
    assert result["percentage"] < 100


def test_invalid_project_path():
    result = validate_project("invalid_project_path_12345")

    assert result["status"] == "FAIL"
    assert result["score"] == "0/6"
    assert result["percentage"] == 0
    assert "Valid project directory" in result["missing_items"]