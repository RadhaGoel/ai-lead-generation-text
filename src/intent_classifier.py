from transformers import pipeline

classifier = pipeline(
    "zero-shot-classification",
    model="facebook/bart-large-mnli"
)

labels = [
    "high intent to buy",
    "asking for product information",
    "just exploring",
    "not interested"
]

def classify_signal(text):
    result = classifier(text, labels)

    return {
        "intent": result["labels"][0],
        "confidence": result["scores"][0]
    }