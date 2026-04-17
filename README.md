# Policy Knowledge Base Builder

A specialized data pipeline for automating the collection and indexing of insurance policy documents from public portals into an AI-ready knowledge base.

## Overview

This toolset is designed to help researchers and individuals systematically analyze complex insurance products. It automates the "dirty work" of scraping scattered PDF documents and transforms them into structured, searchable Markdown files optimized for LLMs (Large Language Models) and AI search engines.

### Key Components

- **Scraper (`src/scraper/main.py`):** A robust crawler that navigates product portals, identifies policy documents (rules, benefit schedules, certificates), and handles downloads with rate limiting.
- **Indexer (`src/indexer/main.py`):** A processing engine that converts binary PDF data into high-quality Markdown, preserving text layouts and international character sets.
- **Config (`src/config.py`):** Centralized management for target URLs, headers, and directory structures.

## Getting Started

### Prerequisites

- Python 3.x
- Virtual Environment (recommended)

### Installation

1. Clone the repository.
2. Initialize a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Usage

1. **Scrape Documents:**
   Run the scraper to download the latest policy PDFs into the `data/raw_pdfs` directory.
   ```bash
   python3 -m src.scraper.main
   ```

2. **Index for AI:**
   Transform the raw PDFs into searchable Markdown in `data/indexed_text`.
   ```bash
   python3 -m src.indexer.main
   ```

## Architecture & Data Safety

- **Data Isolation:** All raw and processed insurance data is stored in the `data/` directory, which is excluded from source control by default.
- **Rate Limiting:** Built-in delays ensure respect for the target server's resources.
- **Context Optimized:** Includes `.gitignore` and context-guardian patterns to ensure efficient AI processing of the codebase.

## License

MIT
