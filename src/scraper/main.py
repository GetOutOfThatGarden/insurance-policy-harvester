import os
import requests
from bs4 import BeautifulSoup
import time
import re
import logging
from src.config import PRODUCT_PAGES, HEADERS, RAW_PDF_DIR

# Setup Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def get_safe_filename(url, download_attr=None):
    """Generates a safe filename from a URL or download attribute."""
    if download_attr:
        return download_attr
    return url.split("/")[-1]

def download_file(url, folder, filename):
    """Downloads a file and saves it to the specified folder."""
    try:
        os.makedirs(folder, exist_ok=True)
        filepath = os.path.join(folder, filename)
        
        if os.path.exists(filepath):
            logger.info(f"Skipping (already exists): {filename}")
            return

        logger.info(f"Downloading: {filename}")
        response = requests.get(url, headers=HEADERS, stream=True, timeout=30)
        response.raise_for_status()
        
        with open(filepath, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        logger.info(f"Successfully downloaded: {filename}")
    except Exception as e:
        logger.error(f"Failed to download {url}: {e}")

def scrape_policy(url):
    """Scrapes a product page for PDF download links."""
    logger.info(f"Processing product page: {url}")
    try:
        response = requests.get(url, headers=HEADERS, timeout=30)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'lxml')
        
        # Extract policy name from URL
        policy_name = url.split("/")[-1].replace(".html", "")
        policy_name = re.sub(r'^\d+-', '', policy_name)
        policy_folder = os.path.join(RAW_PDF_DIR, policy_name)
        
        # Find download links with specific class
        download_links = soup.find_all('a', class_=re.compile(r'btn_download'))
        
        if not download_links:
            # Fallback to any PDF link
            download_links = soup.find_all('a', href=re.compile(r'\.pdf$', re.I))
            
        logger.info(f"Found {len(download_links)} document(s).")
        
        for link in download_links:
            href = link.get('href')
            if not href:
                continue
            
            # Absolute URL resolution
            if href.startswith('/'):
                href = "https://baovietonline.com.vn" + href
            elif not href.startswith('http'):
                # Handle potential relative paths if necessary
                base_product_url = "/".join(url.split("/")[:-1]) + "/"
                href = base_product_url + href
            
            download_attr = link.get('download')
            filename = get_safe_filename(href, download_attr)
            
            download_file(href, policy_folder, filename)
            time.sleep(1) # Rate limiting

    except Exception as e:
        logger.error(f"Error scraping {url}: {e}")

def main():
    """Main entry point for the scraper."""
    os.makedirs(RAW_PDF_DIR, exist_ok=True)
    for page in PRODUCT_PAGES:
        scrape_policy(page)
        time.sleep(2) # Grace period between pages

if __name__ == "__main__":
    main()
