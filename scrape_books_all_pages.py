import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# Step 1: Empty list banao jisme SAARI books ka data store hoga (sab pages se)
book_data = []

# Step 2: 1 se 50 tak loop chalao (kyunki total 50 pages hain)
for page_num in range(1, 51):

    url = f"https://books.toscrape.com/catalogue/page-{page_num}.html"

    # Step 3: Retry logic — agar internet glitch ho to 3 baar dobara try karega
    success = False
    for attempt in range(3):
        try:
            response = requests.get(url, timeout=10)
            response.encoding = "utf-8"
            success = True
            break   # request kaamyaab hui, retry loop se bahar niklo
        except requests.exceptions.ConnectionError:
            print(f"Page {page_num}: internet glitch, retry {attempt + 1}/3...")
            time.sleep(3)   # 3 second ruk ke dobara try karo

    # Agar 3 attempts ke baad bhi fail ho, is page ko skip karke aage badho
    if not success:
        print(f"Page {page_num} skip kar raha hoon (baar baar fail ho raha tha).")
        continue

    if response.status_code != 200:
        print(f"Page {page_num} nahi mila, ruk raha hoon.")
        break

    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("article", class_="product_pod")

    for book in books:
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text
        availability = book.find("p", class_="instock availability").text.strip()

        book_data.append({
            "Title": title,
            "Price": price,
            "Availability": availability
        })

    print(f"Page {page_num} scrape ho gaya... (ab tak total: {len(book_data)} books)")

    time.sleep(1)

# Step 4: Poori list ko DataFrame (table) mein convert karo
df = pd.DataFrame(book_data)

# Step 5: CSV file mein save karo
df.to_csv("books_data_full.csv", index=False, encoding="utf-8-sig")

print("\n✅ Total books scraped:", len(df))
print("\nData 'books_data_full.csv' file mein save ho gaya!")