# DevSecOps Security Analyzer 🛡️🚀

## Overview
This project provides a comprehensive **DevSecOps Security Analyzer** that automates security scanning for dependencies, infrastructure-as-code (IaC), and secrets within a CI/CD pipeline. It features a custom Python-based risk assessment tool that processes repository security datasets to identify and visualize critical risks.

## Architecture
The analyzer integrates multiple security tools into a cohesive pipeline:
1.  **Dependency Scanning (Snyk):** Analyzes `package.json` for known vulnerabilities in third-party libraries.
2.  **Secret Detection (Gitleaks):** Scans the codebase for hardcoded secrets, API keys, and credentials.
3.  **Infrastructure Analysis (Checkov):** Scans Terraform (`main.tf`) for security misconfigurations.
4.  **Custom Security Intelligence (Python Analyzer):** Processes an Excel-based security dataset to calculate risk scores and generate visual reports.

## Tools Integrated
- **Snyk:** Open-source security scanning for vulnerabilities.
- **Gitleaks:** Static analysis tool to find secrets in git repositories.
- **Checkov:** Static code analysis tool for infrastructure-as-code.
- **Python (Pandas & Matplotlib):** For advanced data analysis and visualization.
- **GitHub Actions:** CI/CD orchestration.

## Workflow
1.  **Code Push:** Developers push code to the `main` branch.
2.  **Automated Pipeline Trigger:** GitHub Actions initiates the security workflow.
3.  **Security Scans:** The pipeline concurrently runs Snyk, Checkov, and Gitleaks.
4.  **Risk Analysis:** `devsecops_analyzer_pro.py` executes, calculating risk scores based on severity and public exposure.
5.  **Report Generation:** CSV reports and visualization charts are generated and uploaded as artifacts.

## Risk Scoring Logic
The analyzer uses the following formula to determine risk:
- **High Severity:** 5 points
- **Medium Severity:** 3 points
- **Low Severity:** 1 point
- **Public Exposure:** +5 additional points

### Risk Classification:
- **High Risk:** Score ≥ 8
- **Medium Risk:** Score 4 - 7
- **Low Risk:** Score ≤ 3

## Setup & Usage
1.  **Install Python Dependencies:**
    ```bash
    pip install pandas matplotlib openpyxl
    ```
2.  **Install Security Tools:**
    - [Snyk CLI](https://snyk.io/docs/snyk-cli/)
    - [Checkov](https://www.checkov.io/)
    - [Gitleaks](https://github.com/gitleaks/gitleaks)
3.  **Run Local Analysis:**
    ```bash
    python devsecops_analyzer_pro.py
    ```

## Example Findings (Demo)
- **Vulnerable Dependencies:** Detected in `package.json` (e.g., `lodash@4.17.15`).
- **Secrets:** Detected in `.env` (AWS Secret Key placeholder).
- **IaC Misconfigurations:** Detected in `main.tf` (S3 bucket with public-read ACL).

## Remediation Strategies
- **For Vulnerable Dependencies:** Upgrade to the latest patched version of the library (`npm update`).
- **For Secrets:** Remove hardcoded credentials, rotate affected keys, and use a Secrets Manager (e.g., AWS Secrets Manager or HashiCorp Vault).
- **For IaC Issues:** Implement least-privilege principles, enable encryption, and restrict public access in Terraform configurations.

---
*Created for Academic Submission and Professional DevSecOps Demonstration.*
