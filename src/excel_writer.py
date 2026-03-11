import pandas as pd
from datetime import datetime


def save_leads(leads):

    df = pd.DataFrame(leads)

    df["date_found"] = datetime.now().strftime("%Y-%m-%d")

    df.to_excel("data/leads.xlsx", index=False)

    print("Leads saved to data/leads.xlsx")