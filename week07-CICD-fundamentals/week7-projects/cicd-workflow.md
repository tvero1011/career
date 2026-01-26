## 🔁 CI/CD Workflow with Quality Gates

```mermaid
flowchart LR
    A[Code Push to GitHub] --> B[GitHub Actions Trigger]
    B --> C[Setup Python Environment]
    C --> D[Install Dependencies]
    D --> E[Run flake8 (Linting)]
    E --> F[Run pytest (Testing)]
    F --> G[Run Automation Script]
    G --> H{All Steps Successful?}
    H -- Yes --> I[Pipeline Success ✅]
    H -- No --> J[Pipeline Fails ❌]
