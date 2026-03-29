def classify_patient(symptoms):
    emergency_keywords = [
        "chest pain",
        "breathing",
        "accident",
        "bleeding",
        "unconscious",
        "heart attack"
    ]

    symptoms = symptoms.lower()

    for keyword in emergency_keywords:
        if keyword in symptoms:
            return "EMERGENCY"

    return "NORMAL"