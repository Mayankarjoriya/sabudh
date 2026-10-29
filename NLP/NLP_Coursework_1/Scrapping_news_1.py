import requests
import pandas as pd
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time


# Base Url for indian Expreess Homepage

Base_url = 'https://indianexpress.com'

Headers = {
    'User-Agent' : 'Mozilla/5.0'
}


# Function to get homepage response as html
def get_page(url):
    try:
        reponse = requests.get(url,headers=Headers,timeout=10)

        reponse.raise_for_status()
        return reponse.text
    except requests.RequestException as e:
        print(f"Error: {e}")
        return None


html = get_page(Base_url)

if html is None:
    print("Could not load indian express homepage")
    exit()

# Using BeautifulSoup for extract elements from homepage html
soup = BeautifulSoup(html, 'html.parser')

articles = []

# tag <a> carry href(links) and title
# using urljoin to find relative url for news title
for a in soup.find_all('a',href=True):

    title = a.get_text(strip=True)
    link = a.get('href')

    if not title or not link:
        continue

    link = urljoin(Base_url, link)

    if 'indianexpress.com' in link:

        articles.append({
            'title' : title,
            'link' : link
        })


# Removing same articles if any
unique_articles = {}

for a in articles:
    unique_articles[a['link']] = a

articles = list(unique_articles.values())

# list result carry final data extracted

results =[]

for i,article in enumerate(articles[:30], start=1):

    print(f"Scrapping News: {i}/30")
    article_html = get_page(article['link'])

    if article_html is None:
        continue

    article_soup = BeautifulSoup(
        article_html,
        'html.parser'
    )

    # Paragraph extracts  from article html

    paragraphs = article_soup.find_all('p')

    full_text = " ".join(
        p.get_text(" ", strip=True) for p in paragraphs
    )

    if not full_text:
        continue

    results.append({
        "News_Title": article["title"],
        "News_Link":article['link'],
        "Full_scrappedn_text":full_text
    })

    time.sleep(1)



#  Saving CSV file

df = pd.DataFrame(results)

print(df.head())
print("Total articles:", len(df))

df.to_csv(
    'indian_express_news.csv',
    index=False
)
print('Csv saved succesfully')


