# 💰 Financial Data Parser

A robust Python-based system for parsing and analyzing structured financial data from Excel files. The parser handles multiple file formats, detects data types, normalizes complex financial formats, and stores data in optimized structures for fast querying and aggregation.

---

## 📌 Features

✅ Multi-sheet Excel file processing  
✅ Intelligent data type detection (Date, Number, String)  
✅ Format normalization for messy financial values and dates  
✅ Efficient data storage using dictionaries and indexing  
✅ Querying by date and amount ranges  
✅ Aggregation by category (e.g., credit/debit types)  
✅ Extensible, modular, and clean codebase  

---

## 🛠️ Technologies Used

- Python 3.x
- `pandas` – data processing
- `openpyxl` – Excel reading
- `re` – format matching (regex)
- `datetime` – date conversions

---

## 📂 Project Structure

```bash
financial-data-parser/
│
├── data/
│   └── sample/
│       ├── KH_Bank.XLSX
│       └── Customer_Ledger_Entries_FULL.xlsx
│
├── excel_processor.py       # Phase 1: Excel file reading
├── type_detector.py         # Phase 2: Column type detection
├── format_parser.py         # Phase 3: Date & amount normalization
├── storage.py               # Phase 4: Optimized storage & querying
├── main.py                  # Master script to run all phases
└── README.md

🚀 How to Run
Install Dependencies
pip install pandas openpyxl
Run the Main Script
python main.py
This will:

Load and preview Excel files

Detect column types with confidence scores

Normalize messy amount and date formats

Store data using fast-access indexing

Query and aggregate the results

📸 Sample Output
📋 Column Type Detection
  - Statement.Entry.Amount.Value: number (confidence: 0.92)
  - Statement.Entry.BookingDate.Date: date (confidence: 0.88)
💰 Parsed Amounts
  $1,234.56       → 1234.56
  (2,500.00)      → -2500.0
  1.5M            → 1500000.0
📅 Parsed Dates
  44927           → 2023-01-01
  Q1 2024         → 2024-01-01
📊 Aggregation Example
  Statement.Entry.CreditDebitIndicator   Statement.Entry.Amount.Value
0                                 CRDT                        5.89B
1                                 DBIT                        5.03B
📁 Excel Data Samples
Provided inside data/sample/:

KH_Bank.XLSX

Customer_Ledger_Entries_FULL.xlsx
🧠 Key Learnings
Robust handling of inconsistent financial formats (e.g., ₹1,23,456, 1.2M, (5000.00), etc.)

Column-wise type detection using heuristics and confidence scoring

Range-based filtering using dynamic indexes

Aggregation logic for real-world financial reporting

Clean modular code using OOP principles

📌 Future Improvements
Add SQLite in-memory storage (optional phase)

Improve international format handling (e.g., €1.234,56)

Build a Streamlit dashboard for interactive visualization

Export results to Excel/CSV


