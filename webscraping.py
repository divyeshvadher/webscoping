from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import time
import re
import os

# ---------- CONFIG ----------
START_URL = "https://www.amazon.in"
MAX_PAGES = 500  # max pages to crawl
DELAY = 2        # seconds to wait per page
DOMAIN = urlparse(START_URL).netloc
# ----------------------------

# Headless Chrome
options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

visited = set()
to_visit = set([START_URL])
unique_links = set()

# Buckets for link classification
product_links = set()
category_links = set()
other_links = set()

def is_valid_url(url):
    return url.startswith("http") and DOMAIN in urlparse(url).netloc

def classify_link(url, soup):
    """Classify a link as product, category, or other based on patterns and page structure"""
    if re.search(r"/dp/|/gp/product/", url):  # product URL patterns
        product_links.add(url)
    elif re.search(r"/s\?|/b\?|/category|node=", url):  # category pages
        category_links.add(url)
    else:
        # basic layout heuristic: check for product grid layout
        if soup.select("div.s-main-slot") or soup.select("div.sg-col-4-of-12"):
            category_links.add(url)
        else:
            other_links.add(url)

# Start crawling
while to_visit and len(visited) < MAX_PAGES:
    current_url = to_visit.pop()
    if current_url in visited:
        continue

    print(f"[+] Visiting: {current_url}")
    try:
        driver.get(current_url)
        time.sleep(DELAY)

        soup = BeautifulSoup(driver.page_source, "html.parser")

        for link_tag in soup.find_all("a", href=True):
            href = link_tag['href']
            full_url = urljoin(current_url, href)
            if is_valid_url(full_url):
                if full_url not in visited:
                    to_visit.add(full_url)
                    unique_links.add(full_url)

        classify_link(current_url, soup)
        visited.add(current_url)

    except Exception as e:
        print(f"[!] Error visiting {current_url}: {e}")

driver.quit()

# Save results
os.makedirs("output", exist_ok=True)

def save_links(filename, link_set):
    with open(f"output/{filename}", "w", encoding="utf-8") as f:
        for link in sorted(link_set):
            f.write(link + "\n")

save_links("all_unique_links.txt", unique_links)
save_links("product_links.txt", product_links)
save_links("category_links.txt", category_links)
save_links("other_links.txt", other_links)

print("\n✅ DONE!")
print(f"Total unique links: {len(unique_links)}")
print(f"Products: {len(product_links)} | Categories: {len(category_links)} | Others: {len(other_links)}")
