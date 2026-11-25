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

**Table fields:**

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

**Key capabilities:**
- Calculates total validations performed.
- Counts successful validations.
- Counts failed validations.
- Calculates the overall success percentage.
- Retrieves the latest validation report.

**Analytics endpoint:**

`GET /history/summary`

The summary is calculated dynamically using the stored validation history.

---

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Backend development |
| FastAPI | REST API framework |
| SQLite | Database management |
| SQLAlchemy | Object Relational Mapper (ORM) |
| Pytest | Automated testing |
| Git | Version control |
| GitHub | Source code hosting |
| GitHub Actions | CI workflow |
| Docker | Containerization |
| Terraform | Infrastructure as Code |
| AWS EC2 | Cloud deployment target |
| Prometheus | Monitoring |
| Grafana | Monitoring visualization |

---

## Project Structure

```text
Pipeline-Pilot/
├── .github/
│   └── workflows/
│       └── ci.yml
├── backend/
│   └── app/
│       ├── main.py
│       ├── database/
│       │   ├── __init__.py
│       │   ├── connection.py
│       │   └── models.py
│       ├── services/
│       │   ├── project_validator.py
│       │   ├── validation_history.py
│       │   └── validation_analytics.py
│       └── data/
│           └── validation_history.json
├── docs/
│   └── database-schema.md
├── docker/
├── frontend/
├── monitoring/
│   ├── grafana/
│   └── prometheus/
├── terraform/
├── tests/
│   └── test_pipeline.py
├── .gitignore
├── pytest.ini
├── README.md
└── requirements.txt
```

*Note: The SQLite database file and local validation history data are excluded from version control.*

---

## API Usage

### 1. Validate a Project

**Endpoint:** `POST /validate`

Request:

```json
{
  "project_path": "C:\\path\\to\\project"
}
```

The API checks the project structure and saves the resulting validation report to SQLite.

### 2. Retrieve Validation History

**Endpoint:** `GET /history`

Returns all stored validation reports in newest-first order.

### 3. Retrieve a Specific Report

**Endpoint:** `GET /history/{report_id}`

Returns an individual report using its unique ID.

### 4. Update a Validation Report

**Endpoint:** `PUT /history/{report_id}`

Updates the report associated with the specified ID.

### 5. Delete a Validation Report

**Endpoint:** `DELETE /history/{report_id}`

Deletes the selected validation record.

### 6. Retrieve Validation Analytics

**Endpoint:** `GET /history/summary`

Returns total validations, successful validations, failed validations, success rate, and the latest validation report.

---

## Running the Project Locally

### 1. Clone the repository

```bash
git clone https://github.com/moulika14/Pipeline-Pilot.git
cd Pipeline-Pilot
```

### 2. Create a virtual environment

```bash
py -m venv venv
```

### 3. Activate the environment (Windows)

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Start the backend

```bash
py -m uvicorn backend.app.main:app --reload
```

### 6. Access API documentation

Open:

http://127.0.0.1:8000/docs

Interactive Swagger documentation is available for testing the API endpoints.

---

## Database Documentation

The database schema, table structure, column definitions, and entity relationship diagram are documented here:

- [Database Schema Documentation](docs/database-schema.md)

---

## Testing

Automated tests are implemented using Pytest.

Run the tests:

```bash
py -m pytest -v
```

Previously verified test cases:
- Valid project validation
- Missing requirements detection
- Invalid project path validation

The database integration and CRUD endpoints have also been manually tested through FastAPI Swagger documentation.

---

## Planned Modules

The following modules represent the project's planned development scope and are not yet fully implemented.

1. CI/CD Pipeline Automation
2. Docker Containerization
3. Cloud Deployment
4. Infrastructure Provisioning using Terraform
5. Application Monitoring
6. Deployment Failure Handling and Recovery
7. Deployment Status Dashboard

---

## Development Roadmap

1. Project foundation and structure
2. Project validation and automated testing
3. Validation history and API integration
4. Validation analytics and summary
5. SQLite database integration and CRUD operations
6. CI/CD pipeline enhancements
7. Docker containerization
8. Infrastructure provisioning
9. Cloud deployment
10. Monitoring and visualization
11. Failure handling and recovery

---

## Documentation

Detailed project documentation is available in the `docs/` directory.

- [Project Modules](docs/project-modules.md)
- [Architecture](docs/architecture.md)
- [Requirements](docs/requirements.md)
- [Feature Breakdown](docs/feature-breakdown.md)
- [Module Breakdown](docs/module-breakdown.md)
- [Feature Prioritization](docs/feature-prioritization.md)
- [Development Task List](docs/development-task-list.md)
- [Database Schema](docs/database-schema.md)

---

## Author

**Moulika R**

GitHub: (https://github.com/moulika14)