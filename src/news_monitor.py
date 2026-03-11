import requests

API_KEY = "cdf32e7439a8486bae029bcd82b1d772"

KEYWORDS = [
    "real estate digital transformation",
    "proptech startup",
    "property tech platform",
    "real estate app launch"
]

def fetch_news():

    articles = []

    for keyword in KEYWORDS:

        url = (
            f"https://newsapi.org/v2/everything?"
            f"q={keyword}&"
            f"language=en&"
            f"sortBy=publishedAt&"
            f"apiKey={API_KEY}"
        )

        response = requests.get(url)
        data = response.json()

        if "articles" in data:

            for article in data["articles"][:5]:

                articles.append({
                    "title": article["title"],
                    "link": article["url"],
                    "summary": article["description"]
                })

    return articles