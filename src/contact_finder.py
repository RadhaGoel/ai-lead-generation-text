import requests
from bs4 import BeautifulSoup
import urllib.parse


def find_contact(company_name):

    if company_name is None:
        return {
            "company": None,
            "linkedin_profile": None
        }

    # search query
    query = f"{company_name} CEO LinkedIn"

    url = "https://www.google.com/search?q=" + urllib.parse.quote(query)

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, "html.parser")

    linkedin_url = None

    for link in soup.find_all("a"):
        href = link.get("href")

        if href and "linkedin.com/in/" in href:

            start = href.find("https://")
            end = href.find("&")

            if start != -1:
                linkedin_url = href[start:end]
                break

    # fallback if scraping fails
    if linkedin_url is None:
        linkedin_url = f"https://www.linkedin.com/search/results/people/?keywords={company_name}%20CEO"

    return {
        "company": company_name,
        "linkedin_profile": linkedin_url
    }