
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

## Author
Moulika R
