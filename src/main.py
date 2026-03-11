from news_monitor import fetch_news
from intent_classifier import classify_signal
from lead_scorer import score_lead
from contact_finder import find_contact
from company_finder import extract_company
from excel_writer import save_leads

def main():

    news = fetch_news()

    leads = []

    for article in news:

        title = article["title"]
        summary = article["summary"]

        # STEP 1: extract company from news
        company = extract_company(title)

        # STEP 2: classify intent
        result = classify_signal(summary)

        # STEP 3: score lead
        score = score_lead(result["intent"], result["confidence"])

        # STEP 4: find contact
        contact = find_contact(company)

        #STEP 5: save lead
        lead = {
            "Company": company,
            "Title": title,
            "Intent": result["intent"],
            "Score": score,
            "Linkedin": contact["linkedin_profile"]
        }

        leads.append(lead)

        print("TITLE:", title)
        print("Company:", company)
        print("Intent:", result["intent"])
        print("Score:", score)
        print("LinkedIn:", contact["linkedin_profile"])
        print("-" * 50)

    save_leads(leads)

if __name__ == "__main__":
    main()