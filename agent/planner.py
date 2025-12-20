import os
from google import genai

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

REQUIRED_FIELDS = [
    "name",
    "age",
    "gender",
    "income",
    "bpl",
    "housing_status"
]

PLANNER_PROMPT = """
You are an internal planner for a government scheme assistant.

User text:
{user_text}

Current memory:
{memory}

Contradictions:
{contradictions}

Rules:
- If contradictions exist, output HANDLE_CONTRADICTION
- Ask missing fields in this fixed order:
  name → age → gender → income → bpl → housing_status
- Ask only ONE field at a time
- If all fields are present, output CHECK_ELIGIBILITY

Respond ONLY in one of the following formats:
ASK_MISSING_INFO:<field>
HANDLE_CONTRADICTION
CHECK_ELIGIBILITY
"""

def plan_next_action(user_text, memory_data, contradictions):
    if contradictions:
        return "HANDLE_CONTRADICTION"

    for field in REQUIRED_FIELDS:
        if memory_data.get(field) is None:
            return f"ASK_MISSING_INFO:{field}"

    return "CHECK_ELIGIBILITY"
