import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 1: Website ka URL jisse data nikalna hai
url = "https://books.toscrape.com/"

# Step 2: Website ko request bhejo aur uska HTML page fetch karo
response = requests.get(url)
response.encoding = "utf-8"   # Ye line £ symbol ko sahi tarah decode karegi

# Step 3: Check karo request successful hui ya nahi (200 = OK)
print("Status Code:", response.status_code)

# Step 4: HTML ko BeautifulSoup ke through parse (samajhne layak) banao
soup = BeautifulSoup(response.text, "html.parser")

# Step 5: Har book ek <article class="product_pod"> tag ke andar hoti hai
books = soup.find_all("article", class_="product_pod")

# Step 6: Empty list banao jisme har book ka data store hoga
book_data = []

# Step 7: Har book pe loop chalao aur uska title, price, availability nikalo
for book in books:
    title = book.h3.a["title"]                     # book ka naam
    price = book.find("p", class_="price_color").text   # book ka price
    availability = book.find("p", class_="instock availability").text.strip()  # stock status

    # Step 8: Ye data list mein add karo
    book_data.append({
        "Title": title,
        "Price": price,
        "Availability": availability
    })

# Step 9: List ko pandas DataFrame (table) mein convert karo
df = pd.DataFrame(book_data)

# Step 10: Table ko CSV file mein save karo
df.to_csv("books_data.csv", index=False, encoding="utf-8-sig")   # utf-8-sig Excel ke liye zaroori hai

print("\nTotal books scraped:", len(df))
print("\nPehli 5 books ka data:\n")
print(df.head())
print("\nData 'books_data.csv' file mein save ho gaya!")