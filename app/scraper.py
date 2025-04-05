# scraper.py
import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_shl_catalog():
    url = "https://www.shl.com/en/assessments/catalog/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    data = []
    for item in soup.select(".o-card--product"):
        name = item.select_one(".o-card__title").text.strip()
        description = item.select_one(".o-card__description").text.strip()
        data.append({"name": name, "description": description})

    df = pd.DataFrame(data)
    df.to_csv("app/assessments.csv", index=False)
    print("✅ Scraping done! Saved to app/assessments.csv")

if __name__ == "__main__":
    scrape_shl_catalog()
