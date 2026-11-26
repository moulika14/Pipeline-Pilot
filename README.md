# Pipeline-Pilot
### Cloud-Native CI/CD and Deployment Automation Platform

Pipeline-Pilot is a DevOps automation project designed to simplify project validation and support a structured CI/CD workflow. It aims to automate build verification, testing, containerization, deployment, infrastructure provisioning, and monitoring.

The project currently includes a Python-based project validation system with automated readiness checks, SQLite-backed validation history, CRUD operations, and validation analytics through REST API endpoints.

---

## Project Objectives

- Automate project readiness validation.
- Verify essential project files and infrastructure.
- Integrate automated testing into development workflows.
- Support CI/CD using GitHub Actions.
- Containerize applications using Docker.
- Provision infrastructure using Terraform.
- Support cloud deployment on AWS EC2.
- Monitor application performance using Prometheus and Grafana.
- Maintain validation reports and support future deployment monitoring.

---

## Implemented Features

### 1. Enhanced Project Validator

The validator checks whether a project meets essential requirements before pipeline execution.

**Six validation checks:**
- README.md availability
- requirements.txt availability
- Git repository verification
- Tests directory verification
- Main application file verification
- CI workflow verification

**Validation results include:**
- PASS, WARNING, or FAIL status
- Validation score
- Completion percentage
- Missing requirements
- Project path
- Status message

### 2. SQLite Database Integration

Pipeline-Pilot uses SQLite for persistent storage of project validation history.

**Database details:**
- Database: SQLite
- ORM: SQLAlchemy
- Database file: `backend/app/data/pipeline_pilot.db`
- Table: `validation_records`

| Column | Data Type | Description |
|---|---|---|
| id | VARCHAR | Unique validation record ID (Primary Key) |
| timestamp | VARCHAR | Validation date and time |
| report | JSON | Complete validation report |

The existing JSON validation history was migrated into SQLite. The original JSON file is preserved as a backup.

### 3. Validation History and CRUD Operations

The application supports all four database operations:

- **Create:** Save new validation reports.
- **Read:** Retrieve all reports or a specific report.
- **Update:** Modify an existing validation report.
- **Delete:** Remove a selected validation record.

### 4. REST API Integration

The validation system is integrated with FastAPI.

| Endpoint | Method | Description |
|---|---|---|
| `/` | GET | Displays API service status |
| `/health` | GET | Checks backend health |
| `/validate` | POST | Validates a project and saves the report |
| `/history` | GET | Retrieves all validation reports |
| `/history/summary` | GET | Retrieves validation analytics |
| `/history/{report_id}` | GET | Retrieves a specific report |
| `/history/{report_id}` | PUT | Updates a validation report |
| `/history/{report_id}` | DELETE | Deletes a validation report |

### 5. Validation Analytics and Summary

The analytics feature generates insights from previously stored validation reports.

