# Dynamic URL Crawler

## Project Description

Dynamic URL Crawler is a Python-based asynchronous web scraping tool built using Playwright. This tool is designed to scrape product-related links dynamically from a given list of URLs. It effectively handles infinite scrolling pages and extracts URLs matching specific patterns. The scraped data is stored in a structured JSON format for further use.

## Features

- **Asynchronous Crawling**: Utilizes asyncio and Playwright for high-performance, non-blocking web scraping.
- **Dynamic Scrolling**: Automatically scrolls to the bottom of pages to ensure complete data extraction from infinite scrolling websites.
- **Customizable URL Patterns**: Scrapes links matching specific product-related patterns (e.g., `/product/`, `/dp/`, `/shop/`, etc.).
- **JSON Storage**: Saves extracted product links in a `product_urls.json` file.
- **Scalable Architecture**: Handles multiple URLs concurrently for efficient scraping.

## Installation

### Prerequisites
1. **Python**: Ensure Python 3 or later is installed.

### Steps to Install
1. Clone the repository:
   ```bash
   git clone https://github.com/RaKAsHASH/UrlExtractor.git
   cd UrlExtractor
   ```
2. SetUp a virtual Environment
   ```bash
   python3 -m venv <your-venv-name> 
   ```
3. Activate your virtual Environment
   ```bash
   source ./venv/bin/activate 
   ```
4. Install Dependencies </br>
   **Playwright**: Install and set up Playwright with the following commands:
   ```bash
   pip install playwright
   playwright install
   ```

## Usage

1. Add the target URLs to the `url` list in the script:
   ```python
   url = ["https://www.amazon.in/s?k=i+phone+15+pro", "https://www.flipkart.com/", ...]
   ```
2. Run the script:
   ```bash
   python urlExtractor.py
   ```
3. View the results in the `product_urls.json` file.

## Code Structure

- **`DynamicUrlCrawler` Class**: 
  - Manages the crawling process and data extraction.
- **`start_crawl` Method**: 
  - Initiates the browser, distributes tasks, and manages concurrent URL processing.
- **`scrape_page` Method**: 
  - Handles infinite scrolling and extracts product links.
- **`save_results` Method**: 
  - Saves extracted links to a JSON file.

## Example Output

An example `product_urls.json` file:
```json
{
  "https://www.amazon.in/s?k=i+phone+15+pro": [
    "/product/iphone-15-pro",
    "/dp/B0C7XYZ"
  ],
  "https://www.flipkart.com/": [
    "/item/iphone-case",
    "/p/smartphone"
  ]
}
```

## Dependencies

- Python 3
- [Playwright](https://playwright.dev)

## Limitations

- Limited to scraping product-related links based on predefined patterns.
- Unable to handle Pagination Change to get product Links.
- Static wait time of 2sec for page loading.
- Requires stable internet connection and proper handling of rate limits.


---

Developed with 💻 and 🧠 by Harjeet
