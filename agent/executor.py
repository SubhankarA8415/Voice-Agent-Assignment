from tools.retriever import get_all_schemes
from tools.eligibility import check_eligibility

ODIA_QUESTIONS = {
    "name": "ପ୍ରଥମେ ଆପଣଙ୍କ ନାମ କହନ୍ତୁ ।",
    "age": "ଦୟାକରି ଆପଣଙ୍କ ବୟସ କେତେ?",
    "gender": "ଦୟାକରି ଆପଣଙ୍କ ଲିଙ୍ଗ କହନ୍ତୁ (male/female)?",
    "income": "ଦୟାକରି ଆପଣଙ୍କ ବାର୍ଷିକ ଆୟ କେତେ?",
    "bpl": "ଆପଣ BPL ଶ୍ରେଣୀରେ ଅଛନ୍ତି କି? (true/false)",
    "housing_status": "ଆପଣଙ୍କ ଘର ଅବସ୍ଥା କଣ? (homeless/owned/rented)"
}

def execute_action(planner_action, memory):

    if planner_action == "HANDLE_CONTRADICTION":
        return {
            "type": "CONTRADICTION",
            "text": "ଆପଣଙ୍କ ପୂର୍ବ ତଥ୍ୟରେ ଅସଙ୍ଗତି ମିଳିଛି । ଦୟାକରି ସ୍ପଷ୍ଟ କରନ୍ତୁ ।"
        }

    if planner_action.startswith("ASK_MISSING_INFO"):
        _, field = planner_action.split(":")
        return {
            "type": "ASK",
            "field": field,
            "text": ODIA_QUESTIONS[field]
        }

    if planner_action == "CHECK_ELIGIBILITY":
        schemes = get_all_schemes()
        eligible = []

        for scheme in schemes:
            if check_eligibility(memory.data, scheme):
                eligible.append(scheme)

        return {
            "type": "ELIGIBILITY_RESULT",
            "eligible_schemes": eligible
        }

    return {
        "type": "UNKNOWN",
        "text": "କିଛି ତ୍ରୁଟି ଘଟିଛି ।"
    }
