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

This project uses **Google Gemini API** for the planner module. (gemini-flash 2.5)

## Step 1: Get API Key
- Visit: https://ai.google.dev/
- Generate a free API key

## Step 2: Set Environment Variable

### Windows
```bash
setx GEMINI_API_KEY "your_api_key_here"
Restart the terminal.

macOS / Linux
export GEMINI_API_KEY="your_api_key_here"

⚙️ Local Setup Instructions
Clone Repository
git clone https://github.com/SubhankarA8415/Voice-Agent-Assignment.git
cd voice_scheme_agent

Create Virtual Environment
python -m venv .venv
.venv\Scripts\activate # Windows
source .venv/bin/activate # macOS / Linux

Install Dependencies
pip install -r requirements.txt

Run Application
python app.py
```

## 🎤 Agent Interaction Flow

- Agent greets the user in **Odia**
- Agent collects the following information step by step:
  - **Name**
  - **Age**
  - **Gender**
  - **Annual Income**
  - **BPL Status**
  - **Housing Status**
- After each user response:
  - Agent repeats the transcribed text
  - User confirms with **Yes** or **No**
  - Only confirmed information is stored
- Eligibility is evaluated
- Eligible government schemes are announced
- Agent provides a polite closing message and exits

---

## 🗣️ Recommended Voice Inputs

To minimize STT errors, speak clearly and slowly.

### Examples
- My name is Subhankar.
- My age is 25.
- My gender is male.
- My annual income is two lakhs.
- Yes, I belong to BPL.
- I am homeless.

### Confirmation Responses
- Yes  
- No  

---

## 📜 Government Schemes Included

- **PM Awas Yojana**
- **PM Ujjwala Yojana**
- **Old Age Pension Scheme**

All schemes are defined in `tools/schemes.json` and can be extended easily.

---

## 🧠 Design Highlights

- **Planner–Executor–Evaluator architecture**
- **LLM restricted to decision-making only**
- **Deterministic eligibility logic (no hallucination)**
- **Confirmation loop for speech error handling**
- **Explainable and auditable decisions**

---

## 📊 Evaluation Transcript & Criteria

### Scenario 1: Successful Interaction
- All inputs confirmed successfully  
- Correct eligibility determined  
- **Status:** SUCCESS  

### Scenario 2: Speech Recognition Error
- Incorrect transcription rejected  
- User prompted for re-input  
- **Status:** RECOVERED  

### Scenario 3: Silence / No Input
- Empty input detected  
- User prompted politely  
- **Status:** HANDLED  

### Scenario 4: Contradictory Input
- Conflicting data detected  
- Clarification requested  
- **Status:** HANDLED  

---

## 📏 Evaluation Criteria

- Functional correctness  
- Robust error handling  
- Explainability  
- Agentic design quality  
- User experience  

---

## ✅ Evaluation Summary

| Criterion            | Result |
|----------------------|--------|
| End-to-End Flow      | Passed |
| Error Handling       | Passed |
| Edge Case Handling   | Passed |
| Explainability       | Passed |
| Production Readiness | High   |

---

## 🔮 Future Improvements

- Native Odia speech-to-text  
- Additional government schemes  
- Web or mobile frontend  
- Persistent database storage  
- Cloud deployment  

---

## 👤 Author

**Subhankar Pandit**  
Final Year **B.Tech Computer Science**  

---

## 📄 License

This project is intended for **educational and evaluation purposes only**.

