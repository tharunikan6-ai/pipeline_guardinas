# 🛡️ PIPELINE GUARDIAN: The Autonomous Sentry
> **Where Artificial Intelligence meets DevOps Resilience.**

<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f2027,50:203a43,100:2c5364&height=200&section=header&text=Guardian%20AI&fontSize=40&fontColor=ffffff&animation=fadeIn" />
  <br>
  <img src="https://readme-typing-svg.demolab.com?font=Orbitron&size=24&duration=3000&color=00F7FF&center=true&vCenter=true&width=800&lines=Detecting+Failures...;Analyzing+Logs...;Applying+Fix...;Pipeline+Recovered+✅" />
  <br>
  <h3>⚡ From Reactive Pipelines → Self-Healing Systems</h3>
  <p>🧠 AI-Powered | 🔁 Autonomous | ⚙️ Zero-Touch</p>
</div>

---

## 🌌 The Vision
**Pipeline Guardian** is not just a dashboard; it is a **Neural Engine** designed to bridge the gap between CI/CD failures and engineering exhaustion. It eliminates "Log Fatigue" by utilizing a Large Language Model (LLM) brain to intercept Jenkins failures, perform forensic log analysis, suggest precise fixes, and trigger autonomous recovery actions.

---

## 🏗️ System Architecture: A Unified Organism
Our project is structured as a biological system, unified by a single **Reverse Proxy Gateway**. This ensures the "Brain" and "HUD" operate as a single, cohesive "Proper Website."

### 🕹️ The Components:
* **The HUD (Frontend - Next.js 14):** The sleek, dark-mode **Cyber-HUD** Command Center. Built with Tailwind CSS and Framer Motion for zero-latency visual vitals.
* **The Brain (Backend - FastAPI):** The high-performance Neural Link. It orchestrates the connection between Jenkins raw logs and the GPT-4o reasoning engine.
* **The Sentinel (Jenkins - CI/CD):** The industrial muscle. It handles the builds and provides the data telemetry for the Guardian to analyze.
* **The Gateway (Nginx - Reverse Proxy):** The "Front Door" that merges all services into a single URL (`http://localhost`), providing a professional, unified web experience.

---

## 🔄 The Autonomous "Justice Loop"
1.  **Detect:** Jenkins Sentinel encounters a build failure.
2.  **Intercept:** A Webhook triggers the FastAPI Brain.
3.  **Analyze:** The AI performs Semantic Log Analysis to find the root cause.
4.  **Heal:** The system suggests a fix and triggers an autonomous retry or rollback.
5.  **Notify:** The Cyber-HUD updates and Slack/Discord alerts the team.

---

## 🔬 Research Gaps & Uniqueness
| Feature | Traditional DevOps | Pipeline Guardian (AIOps) |
| :--- | :--- | :--- |
| **Error Handling** | Manual log scrolling | **Autonomous Root Cause Detection** |
| **Response Time** | 30–240 min (MTTR) | **< 2 min (Autonomous)** |
| **Integration** | Fragmented Ports/Tools | **Unified Reverse Proxy Architecture** |
| **Human Effort** | High (On-call stress) | **Zero-Touch Recovery** |

**Exclusive Edge:** Unlike standard monitoring tools that only *alert* you, Guardian AI *understands* the context of the code failure using LLM embeddings, filling the gap between raw data and actionable intelligence.

---

## 🎨 Cyber HUD Dashboard
<p align="center">
  <img src="https://media.giphy.com/media/3o7TKtnuHOHHUjR38Y/giphy.gif" width="700" alt="Cyber HUD Preview"/>
</p>

---

## 🚀 One-Click Deployment (The Docker Way)
Our ecosystem is containerized for total isolation. No "it works on my machine" excuses.

**Prerequisites:**
* Docker Desktop installed.
* OneDrive "Always keep on this device" enabled (if using Windows Desktop).

**The Command of Power:**
```bash
docker-compose up --build
