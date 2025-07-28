from excel_processor import ExcelProcessor
from type_detector import DataTypeDetector
from storage import FinancialDataStore
from datetime import datetime
# ------------------- Phase 1: Excel Processing -------------------

file_paths = [
    r"C:\Users\HP\Desktop\financial-data-parser\data\KH_Bank.XLSX",
    r"C:\Users\HP\Desktop\financial-data-parser\data\Customer_Ledger_Entries_FULL.xlsx"
]

processor = ExcelProcessor()
processor.load_files(file_paths)
processor.get_sheet_info()
from format_parser import FormatParser
import pandas as pd  # Needed for pd.isnull
selected_file = file_paths[0]
sheet_name = "Sheet1"  # Change if your sheet name is different
processor.preview_data(selected_file, sheet_name, rows=5)

# ------------------- Phase 2: Type Detection -------------------

detector = DataTypeDetector()

df = processor.extract_data(selected_file, sheet_name)

print("\n📊 Column Type Detection:")
for col in df.columns:
    result = detector.detect_column_type(df[col])
    print(f"  - {col}: {result['type']} (confidence: {result['confidence']})")
    
# ------------------- Phase 3:  Format Parsing -------------------
    parser = FormatParser()

amount_col = "Statement.Entry.Amount.Value"     
date_col = "Statement.Entry.BookingDate.Date"  
print("\n💰 Normalized Amounts:")
if amount_col in df.columns:
    for val in df[amount_col].head(10):
        print(f"  {val} → {parser.parse_amount(val)}")
else:
    print(f"  ⚠️ Column '{amount_col}' not found in DataFrame.")

print("\n📅 Normalized Dates:")
if date_col in df.columns:
    for val in df[date_col].head(10):
        print(f"  {val} → {parser.parse_date(val)}")
else:
    print(f"  ⚠️ Column '{date_col}' not found in DataFrame.")

 # ------------------- Phase 3: Manual Testing of FormatParser -------------------

print("\n🧪 Manual Test Inputs for FormatParser")

# These are just manual test cases – not related to your Excel file
test_amounts = ["$1,234.56", "(2,500.00)", "€1.234,56", "1.5M", "₹1,23,456", "1234.56-", "2.3K"]
test_dates = ["12/31/2023", "2023-12-31", "Q1 2024", "Dec-23", "44927"]

print("\n💰 Test Amount Parsing:")
for amt in test_amounts:
    print(f"  {amt:>12} → {parser.parse_amount(amt)}")

print("\n📅 Test Date Parsing:")
for d in test_dates:
    print(f"  {d:>12} → {parser.parse_date(d)}")
         # ------------------- Phase 4: Optimized Data Storage & Querying -------------------
store = FinancialDataStore()

# Detect types again using Phase 2 logic
column_types = {}
for col in df.columns:
    result = detector.detect_column_type(df[col])
    column_types[col] = result['type']

# Parse columns using Phase 3 logic
for col, col_type in column_types.items():
    if col_type == 'date':
        df[col] = df[col].apply(parser.parse_date)
    elif col_type == 'number':
        df[col] = df[col].apply(parser.parse_amount)

# Add dataset to the store
store.add_dataset("KH_Bank", df, column_types)

# Example Queries 🔍
# Convert string dates to datetime.date objects
start = datetime.strptime("2023-01-01", "%Y-%m-%d").date()
end = datetime.strptime("2023-12-31", "%Y-%m-%d").date()

print("\n📅 Filter by Date Range:")
print(store.query_by_date_range("KH_Bank", start, end))

print("\n💰 Filter by Amount Range:")
print(store.query_by_amount_range("KH_Bank", 1000, 10000))

print("\n📊 Aggregation Example:")

# Example:
# Group by Credit/Debit type and sum amounts
print(store.aggregate_data(
    "KH_Bank",
    group_by_column="Statement.Entry.CreditDebitIndicator",
    agg_column="Statement.Entry.Amount.Value"
))


