A Python-based web scraping project that extracts detailed car listings from Cars24.com. This scraper collects data such as car name, model, year, price, kilometers driven, fuel type, and location to support analysis of second-hand car trends in India.

🔧 Tech Stack & Tools
Python 3.10+

Selenium (for dynamic content handling)

ChromeDriver (WebDriver for Google Chrome)

Pandas (for data storage and export)

BeautifulSoup (optional: for HTML parsing within dynamic content)

time / random (for throttling requests to avoid detection)

📦 Features
Scrapes multiple pages of car listings

Captures important metadata (price, km driven, fuel type, etc.)

Automatically scrolls and clicks through dynamic content using Selenium

Saves data to CSV or Excel for further analysis

🚧 Challenges Faced
1. Dynamic Content Loading
Issue: Cars24 heavily relies on JavaScript to render car listings. Static scraping with BeautifulSoup was insufficient.

Solution: Integrated Selenium WebDriver to simulate real user behavior and wait for page elements to load.

2. Pagination & Infinite Scrolling
Issue: Cars24 doesn’t use traditional pagination; it loads more content via infinite scrolling.

Solution: Used execute_script() in Selenium to scroll and wait until all listings were loaded.


🗃️ Output
A structured dataset in .csv or .xlsx format

Fields include:

Car Name

Year

Fuel Type

Transmission

Price

Kilometers Driven

Owner Type

Location

▶️ How to Run
Clone the repository:

git clone https://github.com/yourusername/cars24-scraper.git
cd cars24-scraper

Install dependencies:
pip install -r requirements.txt
Run the script:


python cars24_scraper.py
⚠️ Make sure to have Chrome installed and download the matching version of ChromeDriver.

📌 Notes
This project is for educational and research purposes only.

Scraping websites without permission may violate their terms of service. Always check their robots.txt and legal policies before scraping.
