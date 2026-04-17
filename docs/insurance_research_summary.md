# Insurance Research & Comparison Summary (April 2026)

## 🎯 Objective
Research and index BaoViet Insurance policies to find the best health coverage for a 37-year-old non-Vietnamese citizen using an electric motorbike (<4kW) in Vietnam, while factoring in travel to Ireland and other countries.

---

## 🛠 Technical Implementation (Indexing)
The following automated tasks were completed to build a local knowledge base:
- **Web Scraping**: A custom Python scraper (`src/scraper/main.py`) extracted PDF links from 14 BaoViet Personal Insurance product pages.
- **Data Storage**: Raw PDFs are stored in `data/raw_pdfs/`.
- **AI-Ready Indexing**: A text extraction pipeline (`src/indexer/main.py`) converted 6.8MB of PDF content into structured Markdown files in `data/indexed_text/`.
- **Vietnamese Language Support**: The system successfully extracted and preserved Vietnamese diacritics and table structures.

---

## 📊 Insurance Comparison for a 37-Year-Old

### 1. BaoViet Intercare (Select Program)
- **Best For**: High-end local coverage and seamless private hospital access in Vietnam.
- **Annual Price (Inpatient Only)**: ~7,800,000 VND ($310).
- **Limit**: 1.05 Billion VND (~$42k).
- **Direct Billing**: VIP desks at Vinmec, FV, and Family Medical.
- **Motorbike Rule**: Covered without a license if the vehicle is <50cc or the legal equivalent (Your 4kW bike qualifies).

### 2. Genki Traveler (Global Nomad Plan)
- **Best For**: Worldwide flexibility, medical repatriation to Ireland, and massive safety nets.
- **Monthly Price**: €63.70 (~1.7 Million VND).
- **Limit**: €1,000,000 (~27 Billion VND).
- **Motorbike Rule**: Explicitly covers "Light Motorcycles" (<11kW) without a license.
- **Hidden Perks**: Uses **Air Doctor** for cashless clinic visits; covers **Medical Repatriation** to Ireland (flying you home if seriously injured).
- **The "Catch"**: €50 deductible for outpatient visits; 14-day waiting period for non-emergency illnesses if signed up while already in Vietnam.

---

## 🇮🇪 The "Ireland Residency Trap"
- **Vehicle Insurance**: Irish insurers (AXA, Carole Nash) require **Permanent Residency** (185+ days/year in IE). Since you live 8 months/year in Vietnam, local Irish bike insurance is legally invalid for you.
- **Legality**: In Ireland, your 4kW electric bike requires a **Category AM license**. Riding without one is an illegal act that could void your Genki medical coverage.
- **Solution**: When in Ireland, **rent** a motorbike. Rental companies provide the mandatory insurance regardless of your residency, allowing Genki to safely cover your medical bills.

---

## 💡 Final Strategy Recommendation
1. **Primary Plan**: Use **Genki Traveler** as your year-round "Catastrophic" and "Global" safety net.
2. **Local Strategy**: For minor clinic visits (like cat allergies), pay **Cash** in Vietnam. It is cheaper than paying for a second local policy (BaoViet Bronze).
3. **Travel Tip**: Sign up for Genki while still in Ireland to waive the 14-day waiting period.

---

## 📂 Directory Map
- `data/raw_pdfs/`: Original insurance documents.
- `data/indexed_text/`: Searchable Markdown versions of the policies.
- `src/`: Source code for the scraper and indexer.
