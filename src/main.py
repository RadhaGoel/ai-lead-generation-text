from news_monitor import fetch_news

def main():

    print("Program started...")

    news = fetch_news()

    for article in news:
        print(article["title"])
        print(article["link"])
        print()

if __name__ == "__main__":
    main()