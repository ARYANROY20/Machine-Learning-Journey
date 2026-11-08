import threading
import requests
from bs4 import BeautifulSoup

urls = [
    "https://www.google.com",
    "https://www.python.org",
    "https://www.wikipedia.org"
]

def fetch_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    print(f"Fetched {len(soup.text)} characters from {url}")

threads = []

for url in urls:
    thread = threading.Thread(target=fetch_url, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("All Webpages fetched")