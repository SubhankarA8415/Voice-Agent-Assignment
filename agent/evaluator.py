def evaluate_execution(executor_output, memory):
    output_type = executor_output.get("type")

    # Waiting for user input
    if output_type == "ASK":
        return {
            "status": "WAITING_FOR_USER",
            "response_text": executor_output.get("text")
        }

    # Handling contradiction
    if output_type == "CONTRADICTION":
        return {
            "status": "WAITING_FOR_USER",
            "response_text": executor_output.get("text")
        }

    # Eligibility results
    if output_type == "ELIGIBILITY_RESULT":
        schemes = executor_output.get("eligible_schemes", [])

        if not schemes:
            return {
                "status": "COMPLETED",
                "response_text": (
                    "ଦୁଃଖିତ, ଆପଣଙ୍କ ପାଇଁ କୌଣସି ଯୋଗ୍ୟ ସରକାରୀ "
                    "ଯୋଜନା ମିଳିଲା ନାହିଁ । "
                    "ଧନ୍ୟବାଦ।"
                )
            }

        response_lines = [
            "ଆପଣ ନିମ୍ନଲିଖିତ ସରକାରୀ ଯୋଜନାଗୁଡ଼ିକ ପାଇଁ ଯୋଗ୍ୟ ଅଟନ୍ତି:"
        ]

        for scheme in schemes:
            response_lines.append(f"- {scheme['scheme_name']}")
            response_lines.append(f"  ଲାଭ: {scheme['benefits']}")
            response_lines.append(f"  ଆବେଦନ ପ୍ରକ୍ରିୟା: {scheme['apply_steps']}")

        response_lines.append("")
        response_lines.append(
            "ଧନ୍ୟବାଦ। ଆପଣ ଆଉ କିଛି ସହାୟତା ଚାହାନ୍ତି କି?"
        )

        return {
            "status": "COMPLETED",
            "response_text": "\n".join(response_lines)
        }

    # Fallback
    return {
        "status": "FAILED",
        "response_text": "କିଛି ତ୍ରୁଟି ଘଟିଛି । ଦୟାକରି ପୁନଃଚେଷ୍ଟା କରନ୍ତୁ ।"
    }
