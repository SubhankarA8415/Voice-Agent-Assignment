# 🏛️ Voice-Enabled Government Scheme Recommendation Agent

An AI-powered, voice-based assistant that interactively collects user information, confirms inputs to handle speech recognition errors, and recommends eligible Indian government welfare schemes. The system follows a **Planner–Executor–Evaluator** agent architecture and supports voice-based interaction with **Odia responses**.

---

## 🚀 Project Overview

This project demonstrates an end-to-end **agentic AI system** that:

- Interacts with users using voice
- Collects required personal details step by step
- Confirms each input to avoid speech recognition errors
- Uses an LLM strictly for **decision-making only**
- Applies deterministic, rule-based eligibility checks

The system is designed to be **robust, explainable, and production-inspired**.

---

## 🧠 System Architecture

### Agent Lifecycle (End-to-End)

- **User Voice Input**
- **Speech-to-Text (Whisper)**
- **Confirmation Loop**
- **Planner (LLM – decision only)**
- **Executor (tools + logic)**
- **Evaluator (state control)**
- **Text-to-Speech (Odia response)**

---

## 📁 Project Structure

```text
voice_scheme_agent/
├── app.py                  # Main application entry point
├── agent/
│   ├── planner.py          # LLM-based decision logic
│   ├── executor.py         # Executes planner actions
│   ├── evaluator.py        # Validates execution & controls flow
│   └── memory.py           # User profile & conversation memory
├── tools/
│   ├── schemes.json        # Government scheme data
│   ├── eligibility.py     # Rule-based eligibility logic
│   └── retriever.py        # Scheme loader
├── speech/
│   ├── stt.py              # Speech → Text (Whisper)
│   └── tts.py              # Text → Speech (gTTS)
├── requirements.txt
└── README.md
```
# 🛠️ Tech Stack

- **Python 3.9+**
- **faster-whisper** – Speech-to-Text
- **gTTS** – Text-to-Speech
- **Google Gemini API** – Planner (decision only)
- **sounddevice**, **numpy**
- **Rule-based eligibility engine**

---

# 🔑 API Key Setup (Mandatory)

This project uses **Google Gemini API** for the planner module.

## Step 1: Get API Key
- Visit: https://ai.google.dev/
- Generate a free API key

## Step 2: Set Environment Variable

### Windows
```bash
setx GEMINI_API_KEY "your_api_key_here"
Restart the terminal.
