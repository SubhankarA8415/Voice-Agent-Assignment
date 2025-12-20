from speech.stt import listen_and_transcribe
from speech.tts import speak_text

from agent.memory import AgentMemory
from agent.planner import plan_next_action
from agent.executor import execute_action
from agent.evaluator import evaluate_execution
from tools.normalizer import normalize
import time

print("Program started\n")

memory = AgentMemory()

confirmation_words = ["yes", "ha", "haan", "hmm", "yeah", "yep", "ହଁ"]

# ---------- ONE-TIME GREETING ----------
greeting_text = (
    "ନମସ୍କାର! ମୁଁ ସରକାରୀ ଯୋଜନା ସହାୟକ। "
    "ମୁଁ ପଦକ୍ରମେ ଆପଣଙ୍କ ସୂଚନା ନେଇ "
    "ଆପଣ ପାଇଁ ଯୋଗ୍ୟ ସରକାରୀ ଯୋଜନା କହିବି।"
)

print("AGENT (Odia):", greeting_text)
speak_text(greeting_text)

# Allow greeting audio to finish
time.sleep(15)
# -------------------------------------


while True:
    # --------- PLANNER DECIDES NEXT STEP ----------
    action = plan_next_action(
        user_text="",
        memory_data=memory.data,
        contradictions=memory.contradictions
    )
    print("PLANNER:", action)

    # --------- EXECUTOR ----------
    execution = execute_action(action, memory)
    print("EXECUTOR:", execution)

    # ---------- HANDLE FINAL RESULT FIRST ----------
    if execution["type"] == "ELIGIBILITY_RESULT":
        final = evaluate_execution(execution, memory)

        closing_text = (
                final["response_text"]
                + "\n\n"
                + "ଧନ୍ୟବାଦ। ଆପଣ ଆଉ କିଛି ସହାୟତା ଚାହାନ୍ତି କି? "
                  "ନାହିଁ ହେଲେ, ଦୟାକରି Enter ଦବାନ୍ତୁ।"
        )

        print("AGENT (Odia):", closing_text)
        speak_text(closing_text)

        # Allow closing audio to finish
        time.sleep(6)

        input("\nPress Enter to exit...")
        print("\n--- Conversation Completed ---")
        break

    # ---------- NORMAL ASK / CONTRADICTION ----------
    agent_text = execution.get("text", "")
    print("AGENT (Odia):", agent_text)
    speak_text(agent_text)

    # --------- USER ANSWERS ----------
    user_text = listen_and_transcribe()
    print("USER (English):", user_text)

    if not user_text or not user_text.strip():
        agent_text = "ଦୟାକରି ସ୍ପଷ୍ଟ ଭାବେ କହନ୍ତୁ ।"
        print("AGENT (Odia):", agent_text)
        speak_text(agent_text)
        continue

    # --------- CONFIRMATION ----------
    memory.set_pending_confirmation(user_text)
    confirm_text = f"ମୁଁ ଏଭଳି ଶୁଣିଛି: '{user_text}' । ଏହା ଠିକ୍ କି?"
    print("AGENT (Odia):", confirm_text)
    speak_text(confirm_text)

    confirm_response = listen_and_transcribe()
    print("USER (English):", confirm_response)

    if confirm_response.lower().strip().replace(".", "") in confirmation_words:
        field = execution.get("field")
        normalized_value = normalize(field, user_text)

        if normalized_value is None:
            speak_text("ଦୟାକରି ସଠିକ୍ ତଥ୍ୟ ଦିଅନ୍ତୁ ।")
            continue

        memory.update(field, normalized_value)
        memory.clear_pending_confirmation()
        print(f"✔ CONFIRMED {field}: {normalized_value}")

    else:
        memory.clear_pending_confirmation()
        agent_text = "ଠିକ୍ ଅଛି । ଦୟାକରି ପୁନର୍ବାର କହନ୍ତୁ ।"
        print("AGENT (Odia):", agent_text)
        speak_text(agent_text)# Allow rejection message to be heard
        time.sleep(5)
        continue

