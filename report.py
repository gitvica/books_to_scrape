def generate_html_report(books, filename="output.html"):
    with open(filename, "w", encoding="utf-8") as f:
        f.write("<html><head><title>Book Report</title></head><body>")
        f.write("<h1>Books to Scrape Report</h1><ul>")
        for book in books:
            f.write(f"<li><strong>{book['title']}</strong> - {book['price']} ({book['rating']} stars)</li>")
        f.write("</ul></body></html>")

        