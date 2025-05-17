# DevSecOps CI/CD for Python App

### 🛠 Tools Used:
- Flask
- Bandit (SAST)
- OWASP ZAP (DAST)
- GitHub Actions (CI/CD)

### 🔒 Sample vulnerability:
Access: `http://localhost:5000/?name=__import__('os').system('ls')`
