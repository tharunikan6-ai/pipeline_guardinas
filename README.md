# 🛡️ PIPELINE GUARDIAN  
## ⚡ The Autonomous DevOps Sentry  
### 🌌 Where Artificial Intelligence meets DevOps Resilience  

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f2027,50:203a43,100:2c5364&height=220&section=header&text=Pipeline%20Guardian&fontSize=45&fontColor=ffffff&animation=fadeIn"/>
</p>

---

<p align="center">
  🧠 AI-Powered • 🔁 Self-Healing • ⚙️ Zero-Touch DevOps • 🚀 Autonomous CI/CD
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Status-Active-success?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/DevOps-AIOps-blue?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/LLM-Integrated-purple?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/CI/CD-Autonomous-orange?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Architecture-Microservices-red?style=for-the-badge"/>
</p>

---

# 🌌 Vision

Pipeline Guardian transforms CI/CD pipelines into **self-healing autonomous systems powered by AI intelligence**.

It:
- 🧠 Understands pipeline failures  
- 🔍 Detects root causes  
- 🛠️ Suggests fixes  
- ⚡ Automatically recovers pipelines  

---

# 🎯 Problem Statement

| Traditional CI/CD | Limitations |
|------------------|-------------|
| Jenkins Pipelines | Manual debugging |
| Log Files | Overwhelming noise |
| Alerts | No intelligence |
| Recovery | Human dependency |

---

# 💡 Solution

Pipeline Guardian introduces an **AI-powered DevOps intelligence layer**:

✔ Captures pipeline failure events  
✔ Sends logs to LLM engine  
✔ Performs root cause analysis  
✔ Generates fix suggestions  
✔ Executes auto-retry pipeline  

---

# 🏗️ SYSTEM ARCHITECTURE

## 🔄 CI/CD FLOW (Core Engine)

## 🏗️ Isolated, Docker-Orchestrated AIOps Architecture

```mermaid
graph TD

%% ===================== DEVELOPER LAYER =====================
A[Developer] --> B[VS Code Workspace]
B -->|Edit / Build| C[Docker-Compose Engine]

%% ===================== ORCHESTRATION LAYER =====================
subgraph ORCHESTRATION[Docker-Compose Orchestration Layer - Internal Networking]
C --> D[Guardian Gateway Nginx Reverse Proxy]
end

%% ===================== GATEWAY ROUTING =====================
subgraph ROUTING[Unified Web Entry - http://localhost]
D -->|/  : Port 80| E[HUD Frontend Next.js]
D -->|/api: Port 80| F[Brain API FastAPI]
D -->|/jenkins: Port 80| G[Jenkins Sentinel CI/CD]
end

%% ===================== MICROSERVICES LAYER =====================
subgraph SERVICES[Microservices Layer - Python 3.11+ / Next.js 14]
F
G
end

%% ===================== AI INTELLIGENCE LAYER =====================
subgraph AIOPS[AI Ops & Intelligence Layer]
F --> H[Semantic Log Analysis GPT-4o Engine]
F --> I[Root Cause Identification]
I --> J[Autonomous Fix Generator]
end

%% ===================== FEEDBACK LOOP =====================
G -.->|⚠️ Failure Telemetry Webhook| F
J -.->|🛠️ Execute Fix Patch / Trigger Rollback| G
F -.->|📡 Update Feed Framer Motion| E
```
##🧩 MICRO-SERVICES ARCHITECTURE
```mermaid
graph LR
    USER[User] --> NGINX[Nginx Gateway]

    NGINX --> FRONTEND[Frontend Dashboard]
    NGINX --> BACKEND[FastAPI Backend]

    BACKEND --> JENKINS[Jenkins CI/CD]
    BACKEND --> LLM[AI Engine]
```
##🔁 SELF-HEALING LOOP
```mermaid
sequenceDiagram
    participant Jenkins
    participant Backend
    participant AI

    Jenkins->>Backend: Pipeline Failure
    Backend->>AI: Send Logs
    AI->>Backend: Root Cause + Fix
    Backend->>Jenkins: Trigger Auto Retry
```
##⚙️ DEVOPS LIFECYCLE FLOW
```mermaid
flowchart LR
    A[Code Push] --> B[Jenkins Build]
    B --> C{Build Success?}
    C -->|No| D[Failure Detected]
    D --> E[AI Analysis]
    E --> F[Fix Suggested]
    F --> G[Auto Retry]
    C -->|Yes| H[Deployment Success]
```
##  EXECUTION FLOW
```mermaid
 graph TD
    A[1. Developer pushes code] --> B[2. Jenkins pipeline starts]
    B --> C{3. Build Fails?}
    C -->|YES| D[4. Webhook triggers Backend]
    D --> E[5. Logs sent to AI Engine]
    E --> F[6. AI analyzes failure]
    F --> G[7. Root cause detected]
    G --> H[8. Fix is suggested]
    H --> I[9. Pipeline auto-retries]
    I --> J[10. System self-recovers]
    style C fill:#f96,stroke:#333,stroke-width:2px
    style J fill:#00ff00,stroke:#333,stroke-width:4px
```
##📂 PROJECT STRUCTURE
## 📂 PROJECT STRUCTURE

```text
pipeline-guardian/                 <-- Root Folder (Open this in VS Code)
│
├── .gitignore                      # Tells Git what to ignore (node_modules, venv, secrets)
├── docker-compose.yml              # The Master Controller (The "Boss")
├── README.md                       # The Mindblowing Documentation
│
├── 📂 backend/                     # THE BRAIN (Python/FastAPI)
│   ├── main.py                     # Entry point for the API
│   ├── requirements.txt            # Python dependencies
│   ├── Dockerfile                  # Instructions to build the Brain image
│   └── 📂 services/                # Logic for AI, Jenkins connection, etc.
│
├── 📂 frontend/                    # THE HUD (Next.js/React)
│   ├── app/                        # Next.js App Router (pages/components)
│   ├── public/                     # Static assets (logos, icons)
│   ├── package.json                # JS dependencies
│   └── Dockerfile                  # Instructions to build the HUD image
│
├── 📂 infra/                       # THE GATEWAY (Nginx)
│   └── nginx.conf                  # The Routing Logic (The "Front Door")
│
└── 📂 jenkins/                     # THE SENTINEL (CI/CD)
    ├── Dockerfile                  # (Optional) Custom Jenkins setup
    ├── scripts/                    # Your .sh cleanup and fix scripts
    └── 📂 jenkins_data/            # Persistent storage (DO NOT PUSH TO GIT)
```
##🧠 TECH STACK
<p align="center"> <img src="https://skillicons.dev/icons?i=python,fastapi,react,docker,jenkins,nginx,git,github" /> </p>
✨ KEY FEATURES
🔁 Self-healing CI/CD pipelines
🧠 AI log reasoning engine
⚡ Real-time failure detection
🛠️ Auto fix suggestion system
📊 Live DevOps dashboard
🚀 Zero-touch recovery system

📦 One-Click Deployment
# Clone the repository
git clone [https://github.com/tharunikan6-ai/pipeline_guardinas.git](https://github.com/tharunikan6-ai/pipeline_guardinas.git)

# Ignite the Guardian
docker-compose up --build
