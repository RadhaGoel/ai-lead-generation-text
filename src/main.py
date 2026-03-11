from news_monitor import fetch_news
from intent_classifier import classify_signal
from lead_scorer import score_lead


def main():

    news = fetch_news()

    for article in news:

        result = classify_signal(article["summary"])

        score = score_lead(result["intent"], result["confidence"])

        print("TITLE:", article["title"])
        print("Intent:", result["intent"])
        print("Score:", score)
        print("-"*50)


if __name__ == "__main__":
    main()