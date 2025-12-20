# 🏛️ Voice-Enabled Government Scheme Recommendation Agent

An AI-powered, voice-based assistant that interactively collects user information, confirms inputs to handle speech recognition errors, and recommends eligible Indian government welfare schemes. The system follows a Planner–Executor–Evaluator agent architecture and supports voice-based interaction with Odia responses.

---

## 🚀 Project Overview

This project demonstrates an end-to-end **agentic AI system** that:
- Interacts with users using voice
- Collects required personal details step by step
- Confirms each input to avoid speech errors
- Uses an LLM only for decision-making (not hallucination)
- Applies deterministic eligibility rules to recommend government schemes

The system is designed to be **robust, explainable, and production-inspired**.

---

## 🧠 System Architecture

User Voice
↓
Speech-to-Text (Whisper)
↓
Confirmation Loop
↓
Planner (LLM – decision only)
↓
Executor (tools + logic)
↓
Evaluator (state control)
↓
Text-to-Speech (Odia response)

yaml
Copy code

---

## 📁 Project Structure

voice_scheme_agent/
│
├── app.py # Main application entry point
│
├── agent/
│ ├── planner.py # LLM-based decision logic
│ ├── executor.py # Executes planner actions
│ ├── evaluator.py # Validates execution & controls flow
│ └── memory.py # User profile & conversation memory
│
├── tools/
│ ├── schemes.json # Government scheme data
│ ├── eligibility.py # Rule-based eligibility logic
│ └── retriever.py # Scheme loader
│
├── speech/
│ ├── stt.py # Speech → Text (Whisper)
│ └── tts.py # Text → Speech (gTTS)
│
├── requirements.txt
└── README.md

yaml
Copy code

---

## 🛠️ Tech Stack

- Python 3.9+
- faster-whisper (Speech-to-Text)
- gTTS (Text-to-Speech)
- Google Gemini API (Planner only)
- sounddevice + numpy (audio capture)
- Rule-based eligibility engine

---

## 🔑 API Key Setup (Mandatory)

This project uses **Google Gemini API** for the planner module.

### Step 1: Get API Key
Visit: https://ai.google.dev/  
Create a free Gemini API key.

### Step 2: Set Environment Variable

#### Windows (CMD / PowerShell)
```bash
setx GEMINI_API_KEY "your_api_key_here"
Restart the terminal after setting the key.

macOS / Linux
bash
Copy code
export GEMINI_API_KEY="your_api_key_here"
⚙️ Local Setup Instructions
Step 1: Clone Repository
bash
Copy code
git clone https://github.com/your-username/voice_scheme_agent.git
cd voice_scheme_agent
Step 2: Create Virtual Environment (Recommended)
Windows
bash
Copy code
python -m venv .venv
.venv\Scripts\activate
macOS / Linux
bash
Copy code
python3 -m venv .venv
source .venv/bin/activate
Step 3: Install Dependencies
bash
Copy code
pip install -r requirements.txt
Step 4: Ensure Microphone Access
Make sure your system microphone is enabled and accessible.

Step 5: Run the Application
bash
Copy code
python app.py
🎤 How the Agent Works (User Flow)
Agent greets the user in Odia

Agent asks for information step by step:

Name

Age

Gender

Annual Income

BPL Status

Housing Status

After each user response:

The agent repeats what it heard

User confirms with “Yes” or “No”

Only confirmed information is stored

After all details are collected:

Eligibility is evaluated

Eligible government schemes are announced with benefits and application steps

The agent delivers a polite closing message before exiting

🗣️ Recommended Voice Inputs (For Best Accuracy)
Speak clearly and slowly.

Examples:

My name is Subhankar.

My age is 25.

My gender is male.

My annual income is two lakhs.

Yes, I belong to BPL.

I am homeless.

For confirmation, reply only:

Yes

No

📜 Government Schemes Included
PM Awas Yojana

PM Ujjwala Yojana

Old Age Pension Scheme

All schemes are stored in tools/schemes.json and can be easily extended.

🧠 Design Highlights
Planner uses LLM strictly for decision-making

Executor performs deterministic operations

Evaluator manages conversation state

Confirmation loop ensures robustness against speech errors

Eligibility logic is rule-based and explainable

No hallucinated outputs

🎥 Demo
A complete demo video recorded using Loom demonstrates:

Voice interaction

Confirmation handling

Agent lifecycle

Government scheme recommendation

🔮 Future Improvements
Native Odia speech-to-text

More government schemes

Web or mobile frontend

Persistent database storage

Deployment as a hosted service

👤 Author
Subhankar Pandit
Final Year B.Tech Computer Science
AI / ML / Agentic Systems

📄 License
This project is intended for educational and evaluation purposes. keep all these in a single readme.md file not with breaks
