import requests
from bs4 import BeautifulSoup
import json

def scrape_books():
    base_url = "http://books.toscrape.com/"
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    try:
        response = requests.get(base_url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, "html.parser")
        books_data = []

        for book in soup.find_all("article", class_="product_pod"):
            
            title = book.find("h3").find("a")["title"]
            
            price = book.find("p", class_="price_color").get_text()
            
            star_rating_tag = book.find("p", class_="star-rating")
            rating = star_rating_tag["class"][1] if star_rating_tag else "Not Rated"
            
            availability = book.find("p", class_="instock availability").get_text(strip=True)

            books_data.append({
                "title": title,
                "price": price,
                "rating": f"{rating} Stars",
                "availability": availability
            })
            
        return books_data

    except requests.exceptions.RequestException as e:
        print(f"Connection Error: {e}")
        return []

if __name__ == "__main__":
    print("Starting scraper on Books to Scrape...")
    data = scrape_books()
    
    if data:
        print(f"Successfully scraped {len(data)} books.")
        with open("books_data.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
            print("Data saved to books_data.json")
    else:
        print("No data found.")