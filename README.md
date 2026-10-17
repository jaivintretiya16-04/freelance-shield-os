# 🛡️ FreelanceShield OS

An open-weight AI micro-SaaS designed to stop scope creep and unpaid labor for independent freelancers, student creators, and micro-agencies.

[![Hacktoberfest Open-Source AI Challenge](https://img.shields.io/badge/Hacktoberfest-Open_Source_AI-purple?style=for-the-badge)](https://dev.to/challenges/hacktoberfest-week2-2026-10-12)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Groq](https://img.shields.io/badge/Groq-LPU-orange?style=for-the-badge&logo=groq&logoColor=white)](https://groq.com/)

---

## 🚀 What It Does
**FreelanceShield OS** converts messy, informal client chats (WhatsApp/DMs in English or Hinglish) into an ironclad **4-in-1 Business Protection Suite** in under 1.5 seconds:
1. **📄 Official Legal Contract & SoW:** Explicitly defines deliverables, out-of-scope boundaries, revision limits, IP retention, and kill fees.
2. **🧾 Printable Proforma Tax Invoice:** Auto-calculates upfront deposits, milestone breakdowns, and GST/taxes with a 1-click **Print / Save as PDF** feature.
3. **💬 Multi-Channel Pitches:** Ready-to-send onboarding messages in Professional English, natural Hinglish, and Formal Email.
4. **🥊 Scope-Creep Pushback Simulator:** Audits client notes for hidden loopholes and generates polite, firm pushback replies when a client asks for free out-of-scope work.

---

## 🧠 Why Open Innovation Matters
* **100% Confidentiality via Local Ollama:** Freelancers handle sensitive client budgets and NDAs. Running natively via local inference (`http://localhost:11434`) ensures zero client data leaves the freelancer's laptop.
* **Zero Vendor Lock-In & Dynamic Model Swapping:** Built to support open-weight models (Meta Llama 3.1, Gemma 2, Mixtral) with dynamic model fetching to prevent deprecation and rate-limit breakages.
* **Near-Zero Running Costs:** Open-weight inference keeps margins at nearly 100%, making this micro-SaaS commercially viable.

---

## 🛠️ Tech Stack
* **Frontend / UI:** Streamlit (Custom Dark Glassmorphic Theme & CSS Engine)
* **AI Core:** Open-Weight Meta Llama models via **Groq Cloud LPUs** & **Local Ollama**
* **Document Rendering:** HTML5 / CSS3 Print-to-PDF Engine

---

## ⚙️ How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/jaivintretiya16-04/freelance-shield-os.git](https://github.com/jaivintretiya16-04/freelance-shield-os.git)
   cd freelance-shield-os

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   
3. **Run the Streamlit App:**
   ```bash
   python -m streamlit run app.py

📄 License
Distributed under the MIT License. See LICENSE for more information.
