import requests
from bs4 import BeautifulSoup

# Website URL
url = "https://www.bbc.com/news"

# Fetch website HTML
response = requests.get(url)

# Check website response
if response.status_code == 200:

    soup = BeautifulSoup(response.text, "html.parser")

    # Extract headlines
    headlines = soup.find_all("h2")

    # Save headlines in text file
    with open("headlines.txt", "w", encoding="utf-8") as file:

        for i, headline in enumerate(headlines, start=1):

            title = headline.get_text(strip=True)

            if title:
                print(i, title)
                file.write(f"{i}. {title}\n")

    print("\nHeadlines saved successfully!")

else:
    print("Failed to fetch website!")