import feedparser

KEYWORDS = [
    "real estate digital transformation",
    "proptech startup",
    "property tech platform",
    "real estate app launch"
]

def fetch_news():

    articles = []

    for keyword in KEYWORDS:

        url = f"https://news.google.com/rss/search?q={keyword}"

        feed = feedparser.parse(
            url,
            request_headers={
                "User-Agent": "Mozilla/5.0"
            }
        )

        for entry in feed.entries[:5]:

            article = {
                "title": entry.title,
                "link": entry.link,
                "summary": entry.summary
            }

            articles.append(article)

    return articles