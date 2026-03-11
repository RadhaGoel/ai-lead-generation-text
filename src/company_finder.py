from transformers import pipeline

ner = pipeline("ner", model="dslim/bert-base-NER", aggregation_strategy="simple")

def extract_company(text):

    entities = ner(text)

    for entity in entities:
        if entity["entity_group"] == "ORG":
            return entity["word"]

    # fallback: choose first capitalized word longer than 3 letters
    words = text.split()

    for word in words:
        if word[0].isupper() and len(word) > 3:
            return word

    return None