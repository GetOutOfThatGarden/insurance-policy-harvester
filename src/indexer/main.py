import os
import pdfplumber
import logging
from src.config import RAW_PDF_DIR, INDEXED_TEXT_DIR

# Setup Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def extract_text_from_pdf(pdf_path):
    """Extracts text content from a single PDF file."""
    text = ""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n\n"
        return text
    except Exception as e:
        logger.error(f"Error reading {pdf_path}: {e}")
        return None

def process_all_pdfs():
    """Recursively processes all PDFs in RAW_PDF_DIR and saves text to INDEXED_TEXT_DIR."""
    if not os.path.exists(RAW_PDF_DIR):
        logger.warning(f"Raw PDF directory not found: {RAW_PDF_DIR}")
        return

    os.makedirs(INDEXED_TEXT_DIR, exist_ok=True)

    count = 0
    for root, _, files in os.walk(RAW_PDF_DIR):
        # Skip the consolidated All_PDFs folder to avoid duplication
        if "All_PDFs" in root:
            continue
            
        for file in files:
            if file.lower().endswith('.pdf'):
                pdf_path = os.path.join(root, file)
                
                # Maintain parallel folder structure
                relative_path = os.path.relpath(root, RAW_PDF_DIR)
                target_folder = os.path.join(INDEXED_TEXT_DIR, relative_path)
                os.makedirs(target_folder, exist_ok=True)
                
                md_filename = file.replace('.pdf', '.md')
                md_path = os.path.join(target_folder, md_filename)
                
                if os.path.exists(md_path):
                    logger.info(f"Skipping (indexed): {file}")
                    continue

                logger.info(f"Indexing: {file}")
                content = extract_text_from_pdf(pdf_path)
                
                if content:
                    with open(md_path, 'w', encoding='utf-8') as f:
                        f.write(f"# {file}\n\n")
                        f.write(content)
                    count += 1
                else:
                    logger.warning(f"No text extracted from: {file}")

    logger.info(f"Indexing complete. Processed {count} new document(s).")

if __name__ == "__main__":
    process_all_pdfs()
