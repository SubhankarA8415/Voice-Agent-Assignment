import re

def normalize(field, text):
    text = text.lower()

    if field == "name":
        return text.title()

    if field == "age":
        nums = re.findall(r"\d+", text)
        return int(nums[0]) if nums else None

    if field == "income":
        nums = re.findall(r"\d+", text)
        if not nums:
            return None
        value = int(nums[0])
        if "lakh" in text:
            value *= 100000
        return value

    if field == "gender":
        if "male" in text:
            return "male"
        if "female" in text:
            return "female"
        return None

    if field == "bpl":
        if "yes" in text or "true" in text:
            return True
        if "no" in text or "false" in text:
            return False
        return None

    if field == "housing_status":
        if "homeless" in text:
            return "homeless"
        if "rent" in text:
            return "rented"
        if "own" in text:
            return "owned"
        return None

    return text
