# CodeAlpha_WebScraping

## 📌 Task 1 — Web Scraping | CodeAlpha Data Analytics Internship

This project scrapes book data from [Books to Scrape](https://books.toscrape.com/), a public sandbox website designed for practicing web scraping.

## 🎯 Objective
Extract book information (title, price, and stock availability) from all 50 pages of the website and store it in a structured CSV file for further analysis.

## 🛠️ Tools & Libraries Used
- **Python 3**
- **Requests** — to fetch web pages
- **BeautifulSoup4** — to parse HTML and extract data
- **Pandas** — to structure and save data as CSV

## 📂 Project Files
| File | Description |
|------|-------------|
| `scrape_books.py` | Scrapes book data from a single page (basic version) |
| `scrape_books_all_pages.py` | Scrapes book data from all 50 pages with retry logic for connection errors |
| `books_data_full.csv` | Final dataset containing 1000 scraped books |

## ⚙️ How It Works
1. Sends an HTTP request to each page of the website.
2. Parses the HTML response using BeautifulSoup.
3. Extracts the book **title**, **price**, and **availability** for each listing.
4. Stores all records in a Pandas DataFrame.
5. Saves the final dataset as a CSV file.

Includes retry logic to automatically handle temporary internet/connection interruptions during scraping.

## 📊 Output
The final dataset (`books_data_full.csv`) contains **1000 books** with the following columns:
- `Title`
- `Price`
- `Availability`

## ▶️ How to Run
```bash
pip install requests beautifulsoup4 pandas
python scrape_books_all_pages.py
```

## 🙋 Author
Muhammad Hashir — CodeAlpha Data Analytics Intern

## 🏢 About CodeAlpha
This project was completed as part of the **CodeAlpha Data Analytics Internship**.
Website: [www.codealpha.tech](https://www.codealpha.tech)