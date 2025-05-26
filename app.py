
from flask import Flask, send_file, render_template_string
import os
from scraper import scrape_books
from report import generate_html_report

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <html>
    <head>
        <title>Book Scraper Dashboard</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; }
            .container { max-width: 800px; margin: 0 auto; }
            .button { 
                background-color: #4CAF50; 
                color: white; 
                padding: 15px 32px; 
                text-decoration: none; 
                display: inline-block; 
                font-size: 16px; 
                margin: 4px 2px; 
                cursor: pointer; 
                border-radius: 4px;
            }
            .button:hover { background-color: #45a049; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>📚 Books to Scrape Dashboard</h1>
            <p>Welcome to the book scraper dashboard. Use the buttons below to interact with the system.</p>
            <a href="/scrape" class="button">🔄 Scrape New Data</a>
            <a href="/report" class="button">📖 View Report</a>
        </div>
    </body>
    </html>
    '''

@app.route('/scrape')
def scrape():
    try:
        books = scrape_books()
        generate_html_report(books)
        return '''
        <html>
        <head>
            <title>Scraping Complete</title>
            <style>
                body { font-family: Arial, sans-serif; margin: 40px; }
                .container { max-width: 800px; margin: 0 auto; }
                .success { color: #4CAF50; font-size: 18px; }
                .button { 
                    background-color: #4CAF50; 
                    color: white; 
                    padding: 15px 32px; 
                    text-decoration: none; 
                    display: inline-block; 
                    font-size: 16px; 
                    margin: 4px 2px; 
                    cursor: pointer; 
                    border-radius: 4px;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>✅ Scraping Complete!</h1>
                <p class="success">Successfully scraped and generated report for ''' + str(len(books)) + ''' books.</p>
                <a href="/report" class="button">📖 View Report</a>
                <a href="/" class="button">🏠 Back to Dashboard</a>
            </div>
        </body>
        </html>
        '''
    except Exception as e:
        return f'''
        <html>
        <body style="font-family: Arial, sans-serif; margin: 40px;">
            <h1>❌ Error</h1>
            <p>An error occurred while scraping: {str(e)}</p>
            <a href="/" style="color: #4CAF50;">← Back to Dashboard</a>
        </body>
        </html>
        '''

@app.route('/report')
def report():
    try:
        if os.path.exists('output.html'):
            return send_file('output.html')
        else:
            return '''
            <html>
            <body style="font-family: Arial, sans-serif; margin: 40px;">
                <h1>📋 No Report Found</h1>
                <p>No report has been generated yet. Please scrape data first.</p>
                <a href="/scrape" style="color: #4CAF50;">🔄 Scrape Data</a> | 
                <a href="/" style="color: #4CAF50;">🏠 Back to Dashboard</a>
            </body>
            </html>
            '''
    except Exception as e:
        return f'''
        <html>
        <body style="font-family: Arial, sans-serif; margin: 40px;">
            <h1>❌ Error</h1>
            <p>An error occurred while loading the report: {str(e)}</p>
            <a href="/" style="color: #4CAF50;">← Back to Dashboard</a>
        </body>
        </html>
        '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
