import os

# Base Directories
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
RAW_PDF_DIR = os.path.join(DATA_DIR, "raw_pdfs")
INDEXED_TEXT_DIR = os.path.join(DATA_DIR, "indexed_text")

# Scraper Settings
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

PRODUCT_PAGES = [
    "https://baovietonline.com.vn/en/product-personal/1/bao-viet-an-gia-insurance.html",
    "https://baovietonline.com.vn/en/product-personal/56/bao-viet-tam-binh-insurance.html",
    "https://baovietonline.com.vn/en/product-personal/19/intercare-insurance.html",
    "https://baovietonline.com.vn/en/product-personal/57/hospital-cash-insurance.html",
    "https://baovietonline.com.vn/en/product-personal/2/cancer-insurance.html",
    "https://baovietonline.com.vn/en/product-personal/4/10-critical-illness-insurance.html",
    "https://baovietonline.com.vn/en/product-personal/58/37-critical-illness-insurance.html",
    "https://baovietonline.com.vn/en/product-personal/5/human-accident-insurance.html",
    "https://baovietonline.com.vn/en/product-personal/10/domestic-travel-insurance.html",
    "https://baovietonline.com.vn/en/product-personal/9/flexi-travel-insurance.html",
    "https://baovietonline.com.vn/en/product-personal/54/comprehensive-vehicle-insurance.html",
    "https://baovietonline.com.vn/en/product-personal/6/automotive-civil-liability-insurance.html",
    "https://baovietonline.com.vn/en/product-personal/7/motorbike-civil-liability-insurance.html",
    "https://baovietonline.com.vn/en/product-personal/8/home-insurance.html"
]
