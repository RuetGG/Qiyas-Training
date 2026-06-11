import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.thereporterethiopia.com"
response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
soup = BeautifulSoup(response.text, "html.parser")

headlines = []
data = []

for article in soup.find_all("h3"):
    title = article.get_text(strip=True)
    if title:
        headlines.append({
            "title": title
        })
    link = article.find("a")
    if link:
        title = link.get_text(strip=True)
        href = link.get("href")
        data.append({
            "title": title,
            "url": href
        })
        
print("Collected:", len(headlines))
df = pd.DataFrame(data)
df.to_csv("Web_Scraping/ethiopian_news.csv", index=False)
print("Saved:", len(df))

print(df.head())