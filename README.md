# Pipeline-Pilot
### Cloud-Native CI/CD and Deployment Automation Platform

Pipeline-Pilot is a DevOps automation project designed to simplify project validation and support a structured CI/CD workflow. It aims to automate build verification, testing, containerization, deployment, infrastructure provisioning, and monitoring.

The project currently includes a Python-based project validation system with automated readiness checks and persistent validation history through REST API endpoints.

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

### 2. Validation History

The system stores validation reports locally in JSON format.

Each record contains:
- Unique report ID
- Timestamp
- Validation result
- Project readiness score
- Missing requirements

### 3. REST API Integration

The validation system is integrated with FastAPI, enabling users to validate projects and retrieve saved reports through API endpoints.

| Endpoint | Method | Description |
|---|---|---|
| `/` | GET | Displays API service status |
| `/health` | GET | Checks backend health |
| `/validate` | POST | Validates a project and saves the report |
| `/history` | GET | Retrieves all saved validation reports |
| `/history/{report_id}` | GET | Retrieves a specific report by ID |

---

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Backend development |
| FastAPI | REST API framework |
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
│       ├── services/
│       │   ├── project_validator.py
│       │   └── validation_history.py
│       └── data/
│           └── validation_history.json
├── docker/
├── docs/
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

*Note: The validation history JSON file is generated locally at runtime and is excluded from version control.*

---

## API Usage

### Validate a Project

**Endpoint:** `POST /validate`

Request:

```json
{
  "project_path": "C:\\path\\to\\project"
}
```

The API checks the project structure and returns a validation report. Successful validation reports are automatically saved to the history system.

### Retrieve Validation History

**Endpoint:** `GET /history`

Returns the total number of stored reports and the validation records in newest-first order.

### Retrieve a Specific Report

**Endpoint:** `GET /history/{report_id}`

Returns an individual report using its unique ID.

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

### 6. Access the API documentation

Open:

http://127.0.0.1:8000/docs

Interactive Swagger documentation is available for testing the API endpoints.

---

## Testing

Automated tests are implemented using Pytest.

Run the tests:

```bash
py -m pytest -v
```

**Current test results:**
- Valid project validation — Passed
- Missing requirements detection — Passed
- Invalid project path validation — Passed

**Latest verified result: 3 tests passed.**

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

The project follows a phased development approach:

1. Project foundation and structure
2. Project validation and automated testing
3. Validation history and API integration
4. CI/CD pipeline enhancements
5. Docker containerization
6. Infrastructure provisioning
7. Cloud deployment
8. Monitoring and visualization
9. Failure handling and recovery

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

---

## Author

**Moulika R**

GitHub: [moulika14](https://github.com/moulika14)
