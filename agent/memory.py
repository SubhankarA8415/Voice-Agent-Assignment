class AgentMemory:
    def __init__(self):
        self.data = {
            "name": None,
            "age": None,
            "income": None,
            "gender": None,
            "bpl": None,
            "housing_status": None
        }
        self.contradictions = []
        self.state = "collecting_info"
        self.history = []

        self.pending_confirmation = None

    def update(self, key, value):
        if key in self.data and self.data[key] is not None:
            if self.data[key] != value:
                self.contradictions.append(
                    f"Contradiction detected for {key}: "
                    f"previous={self.data[key]}, new={value}"
                )
        self.data[key] = value

    def get(self, key):
        return self.data.get(key)

    def is_complete(self):
        return all(v is not None for v in self.data.values())

    def has_contradictions(self):
        return len(self.contradictions) > 0

    def reset_contradictions(self):
        self.contradictions = []

    # Confirmation helpers
    def set_pending_confirmation(self, text):
        self.pending_confirmation = text

    def clear_pending_confirmation(self):
        self.pending_confirmation = None

    def has_pending_confirmation(self):
        return self.pending_confirmation is not None
