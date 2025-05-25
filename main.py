from scraper import scrape_books
from report import generate_html_report

def main():
    books = scrape_books()
    generate_html_report(books)
    print("✅ Report generated: output.html")

if __name__ == "__main__":
    main()