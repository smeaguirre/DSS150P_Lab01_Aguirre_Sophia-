import os
from pathlib import Path
import pandas as pd

RAW = Path("data")

# Load the sources
customers = pd.read_csv(RAW / "customers.csv")
orders = pd.read_json(RAW / "orders.json")
products = pd.read_parquet(RAW / "products.parquet")

files_to_profile = {
    "customers.csv": customers,
    "orders.json": orders,
    "products.parquet": products,
}

for name, df in files_to_profile.items():
    file_path = RAW / name
    # 1. File name and file size in KB
    file_size_kb = file_path.stat().st_size / 1024 if file_path.exists() else 0
    
    print(f"\n{'='*50}")
    print(f"=== {name} ===")
    print(f"File Size: {file_size_kb:.2f} KB")
    
    # 2. Number of rows and columns
    print(f"Shape (Rows, Columns): {df.shape}")
    
    # 3. Column names in original order
    print(f"Columns: {list(df.columns)}")
    
    # 4. Inferred data type of every column
    print("\n--- Data Types ---")
    print(df.dtypes)
    
    # 5. Number of missing/null values per column
    print("\n--- Missing/Null Values ---")
    print(df.isna().sum())
    
    # 6. Number of fully duplicated rows (exclude unhashable/dict columns like 'shipping')
    try:
        dup_count = df.duplicated().sum()
    except TypeError:
        hashable_cols = [c for c in df.columns if not df[c].apply(lambda x: isinstance(x, (dict, list))).any()]
        dup_count = df.duplicated(subset=hashable_cols).sum()
    print(f"\nFully Duplicated Rows: {dup_count}")
    
    # 7. Number of distinct values per column
    print("\n--- Distinct Values per Column ---")
    for col in df.columns:
        try:
            print(f"  {col}: {df[col].nunique()}")
        except TypeError:
            print(f"  {col}: [Nested Object/Dict - Cannot count unique directly]")
    
    # 9. Numeric columns: min and max values
    numeric_cols = df.select_dtypes(include='number').columns
    if not numeric_cols.empty:
        print("\n--- Numeric Ranges ---")
        for col in numeric_cols:
            print(f"  {col}: Min = {df[col].min()}, Max = {df[col].max()}")
            
    # 10. Date/time-like columns: earliest and latest (safe parsing)
    print("\n--- Date/Time Ranges ---")
    date_found = False
    for col in df.columns:
        if pd.api.types.is_datetime64_any_dtype(df[col]) or any(k in col.lower() for k in ['date', 'time', 'timestamp']):
            try:
                parsed_dates = pd.to_datetime(df[col], errors='coerce')
                if parsed_dates.notna().any():
                    print(f"  {col}: Earliest = {parsed_dates.min()}, Latest = {parsed_dates.max()}")
                    date_found = True
            except Exception:
                pass
    if not date_found:
        print("  No date/time columns detected or parsed.")

    # 8. First five records
    print("\n--- First 5 Records ---")
    print(df.head())
    print(f"{'='*50}\n")