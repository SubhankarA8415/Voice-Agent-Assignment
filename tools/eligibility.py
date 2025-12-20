def check_eligibility(user_profile, scheme):
    criteria = scheme.get("criteria", {})

    for key, value in criteria.items():
        if key == "income_max":
            if user_profile.get("income", float("inf")) > value:
                return False

        elif key == "age_min":
            if user_profile.get("age", 0) < value:
                return False

        elif key == "gender":
            if user_profile.get("gender") != value:
                return False

        elif key == "bpl":
            if user_profile.get("bpl") != value:
                return False

        elif key == "housing_status":
            if user_profile.get("housing_status") != value:
                return False

    return True
