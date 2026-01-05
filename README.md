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

# 📊 Evaluation Transcript & Criteria

This section documents the evaluation of the **Voice-Enabled Government Scheme Recommendation Agent**, including successful interactions, failed interactions, and edge-case handling. The goal is to demonstrate robustness, correctness, and real-world readiness of the agent.

---

## ✅ Evaluation Scenario 1: Successful Interaction (Happy Path)

### User Profile
- Name: Subhankar
- Age: 25
- Gender: Male
- Annual Income: 2 Lakhs
- BPL Status: Yes
- Housing Status: Homeless

### Interaction Transcript

**AGENT (Odia):**  
ନମସ୍କାର! ମୁଁ ସରକାରୀ ଯୋଜନା ସହାୟକ। ମୁଁ ପଦକ୍ରମେ ଆପଣଙ୍କ ସୂଚନା ନେଇ ଆପଣ ପାଇଁ ଯୋଗ୍ୟ ସରକାରୀ ଯୋଜନା କହିବି।

**AGENT:** ପ୍ରଥମେ ଆପଣଙ୍କ ନାମ କହନ୍ତୁ ।  
**USER:** My name is Subhankar.  
**AGENT:** ମୁଁ ଏଭଳି ଶୁଣିଛି: ‘My name is Subhankar’. ଏହା ଠିକ୍ କି?  
**USER:** Yes.

**AGENT:** ଦୟାକରି ଆପଣଙ୍କ ବୟସ କେତେ?  
**USER:** My age is 25.  
**AGENT:** ଏହା ଠିକ୍ କି?  
**USER:** Yes.

**AGENT:** ଦୟାକରି ଆପଣଙ୍କ ଲିଙ୍ଗ କହନ୍ତୁ।  
**USER:** My gender is male.  
**AGENT:** ଏହା ଠିକ୍ କି?  
**USER:** Yes.

**AGENT:** ଦୟାକରି ଆପଣଙ୍କ ବାର୍ଷିକ ଆୟ କେତେ?  
**USER:** My annual income is two lakhs.  
**AGENT:** ଏହା ଠିକ୍ କି?  
**USER:** Yes.

**AGENT:** ଆପଣ BPL ଶ୍ରେଣୀରେ ଅଛନ୍ତି କି?  
**USER:** Yes, I belong to BPL.  
**AGENT:** ଏହା ଠିକ୍ କି?  
**USER:** Yes.

**AGENT:** ଆପଣଙ୍କ ଘର ଅବସ୍ଥା କଣ?  
**USER:** I am homeless.  
**AGENT:** ଏହା ଠିକ୍ କି?  
**USER:** Yes.

**AGENT (Result):**  
ଆପଣ PM Awas Yojana ପାଇଁ ଯୋଗ୍ୟ ଅଟନ୍ତି।  
ଲାଭ: ବାସଗୃହ ନିର୍ମାଣ ପାଇଁ ଆର୍ଥିକ ସହାୟତା  
ଆବେଦନ ପ୍ରକ୍ରିୟା: pmay.gov.in କିମ୍ବା ନିକଟତମ CSC କେନ୍ଦ୍ର

**Status:** ✅ SUCCESS

---

## ❌ Evaluation Scenario 2: Failed Confirmation (Speech Error Handling)

### Scenario
Speech recognition produces incorrect transcription.

### Interaction Transcript

**USER:** My annual income is two lakhs.  
**AGENT:** ମୁଁ ଏଭଳି ଶୁଣିଛି: ‘My annual income is $2000’. ଏହା ଠିକ୍ କି?  
**USER:** No.  

**AGENT:** ଠିକ୍ ଅଛି। ଦୟାକରି ପୁନର୍ବାର କହନ୍ତୁ।

**USER:** My annual income is two lakhs.  
**AGENT:** ଏହା ଠିକ୍ କି?  
**USER:** Yes.

**Status:** ⚠️ RECOVERED SUCCESSFULLY

### Observation
- Incorrect STT output was rejected
- Agent requested re-input
- No incorrect data stored

---

## ⚠️ Evaluation Scenario 3: Edge Case – Silence / No Input

### Scenario
User does not speak or microphone input is empty.

### Interaction Transcript

**AGENT:** ଦୟାକରି ଆପଣଙ୍କ ବୟସ କହନ୍ତୁ।  
**USER:** (silence)

**AGENT:** ଦୟାକରି ସ୍ପଷ୍ଟ ଭାବେ କହନ୍ତୁ।

**Status:** ⚠️ HANDLED GRACEFULLY

### Observation
- System detects empty input
- Does not crash
- Politely asks user to repeat

---

## ⚠️ Evaluation Scenario 4: Edge Case – Contradictory Input

### Scenario
User provides conflicting information.

### Interaction Transcript

**USER:** My age is 25.  
**USER (later):** My age is 40.

**AGENT:**  
ଆପଣଙ୍କ ପୂର୍ବ ତଥ୍ୟରେ ଅସଙ୍ଗତି ମିଳିଛି। ଦୟାକରି ସ୍ପଷ୍ଟ କରନ୍ତୁ।

**Status:** ⚠️ CONTRADICTION DETECTED AND HANDLED

---

## 📏 Evaluation Criteria

The system was evaluated using the following criteria:

### 1. Functional Correctness
- Correct collection of required user attributes
- Accurate eligibility determination
- Deterministic rule-based scheme matching

### 2. Robustness
- Handles speech recognition errors via confirmation loop
- Recovers from silence and unclear input
- Detects contradictory information

### 3. Explainability
- Clear reasoning for scheme eligibility
- Transparent prompts and actions
- Deterministic decision flow

### 4. Agent Design Quality
- Planner–Executor–Evaluator separation
- LLM restricted to decision-making only
- No hallucinated outputs

### 5. User Experience
- Step-by-step questioning
- Voice + text feedback
- Polite and clear Odia responses
- Graceful conversation closure

---

## ✅ Evaluation Summary

| Criterion            | Result    |
|----------------------|-----------|
| End-to-End Flow      | ✅ Passed |
| Error Handling       | ✅ Passed |
| Edge Case Handling   | ✅ Passed |
| Explainability       | ✅ Passed |
| Production Readiness | ✅ High   |

The system meets all functional and non-functional requirements specified in the assignment and demonstrates a robust, production-inspired agentic AI design. 

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
**Full Stack Developer | Backend Engineer | AI/ML | Cloud**  
**GitHub**: https://github.com/SubhankarA8415  
**LinkedIn**: https://linkedin.com/in/subhankar-pandit 

---

## 📄 License

This project is intended for **educational and evaluation purposes only**.



