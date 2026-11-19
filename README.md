
# PipelinePilot
### Cloud-Native CI/CD and Deployment Automation Platform

PipelinePilot is a DevOps project designed to automate application build, testing, containerization, cloud deployment, infrastructure provisioning, and monitoring.

## Project Objectives
- Automate build and testing using GitHub Actions.
- Containerize applications using Docker.
- Deploy applications on AWS EC2.
- Provision infrastructure using Terraform.
- Monitor application performance using Prometheus and Grafana.
- Detect deployment failures and support notifications and rollback.
- Provide a dashboard for deployment status and application health.

## Technology Stack
- **Programming:** Python, Bash
- **Backend:** FastAPI
- **Version Control:** Git and GitHub
- **CI/CD:** GitHub Actions
- **Containerization:** Docker
- **Cloud:** AWS EC2
- **Infrastructure as Code:** Terraform
- **Monitoring:** Prometheus and Grafana

## Project Modules
1. CI/CD Pipeline
2. Docker Containerization
3. Cloud Deployment
4. Infrastructure as Code
5. Application Monitoring
6. Failure Handling
7. Deployment Dashboard

## Project Structure
```text
Pipeline-Pilot/
├── .github/
│   └── workflows/
├── backend/
│   └── app/
│       ├── routes/
│       └── services/
├── docker/
├── docs/
├── frontend/
├── monitoring/
│   ├── grafana/
│   └── prometheus/
├── terraform/
├── tests/
├── .gitignore
├── README.md
└── requirements.txt
```

## Documentation
- [Project Modules](docs/project-modules.md)
- [Architecture Diagram](docs/architecture.md)

## Development Status
Project structure and initial documentation are being organized. Implementation will follow the planned development sequence.

## Requirements & Development Planning

PipelinePilot follows a structured development approach to ensure that requirements, features, modules and implementation tasks are clearly defined before development.

### Project Documentation

The `docs/` directory contains the project planning and technical documentation.

| Document | Description |
|---|---|
| `architecture.md` | Proposed system architecture and workflow |
| `project-modules.md` | Overview of the main project modules |
| `requirements.md` | Functional, non-functional and user requirements |
| `feature-breakdown.md` | Feature descriptions, inputs, processing and outputs |
| `module-breakdown.md` | Module responsibilities, dependencies and communication |
| `feature-prioritization.md` | Feature classification based on implementation priority |
| `development-task-list.md` | Step-by-step development roadmap |

### Development Strategy

Development will follow a priority-based approach:

1. Establish the application foundation.
2. Implement the CI/CD pipeline and automated testing.
3. Containerize the application using Docker.
4. Provision cloud infrastructure using Terraform.
5. Deploy the application to AWS EC2.
6. Integrate monitoring using Prometheus and Grafana.
7. Implement failure handling and recovery.
8. Develop and integrate the deployment dashboard.

The core deployment workflow will be implemented and validated before proceeding with additional enhancements.

## Author
Moulika R
