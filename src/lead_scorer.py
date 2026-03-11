def score_lead(intent, confidence):

    if intent == "high intent to buy":
        return int(confidence * 100)

    if intent == "asking for product information":
        return int(confidence * 80)

    if intent == "just exploring":
        return int(confidence * 40)

    return int(confidence * 10)