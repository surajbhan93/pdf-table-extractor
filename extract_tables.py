# Step 1: Import Required Modules
import pdfplumber
import pandas as pd
import os

# Step 2: Define Function to Extract Tables from PDF
def extract_tables_from_pdf(pdf_path):
    tables = []
    
    with pdfplumber.open(pdf_path) as pdf:
        for page_number, page in enumerate(pdf.pages, start=1):
            tables_on_page = page.extract_tables()
            print(f"Page {page_number}: Found {len(tables_on_page)} tables")  # Debugging info
            
            if tables_on_page:
                for idx, table in enumerate(tables_on_page, start=1):
                    df = pd.DataFrame(table)
                    
                    if df.empty:
                        continue
                    
                    df.columns = df.iloc[0]  # Set first row as column headers
                    df = df[1:]  # Remove header from data
                    df.reset_index(drop=True, inplace=True)
                    tables.append((page_number, idx, df))
    
    return tables

# Step 3: Save Extracted Tables to CSV Files
def save_tables(tables, output_dir="output"):
    os.makedirs(output_dir, exist_ok=True)
    
    for page_number, table_index, df in tables:
        output_file = f"{output_dir}/table_page_{page_number}_table_{table_index}.csv"
        df.to_csv(output_file, index=False)
        print(f"✅ Saved: {output_file}")

# Step 4: Run the Script
if __name__ == "__main__":
    pdf_path = "test3.pdf"  # Replace this with your own PDF filename
    tables = extract_tables_from_pdf(pdf_path)
    
    if tables:
        save_tables(tables)
    else:
        print("❌ No tables found in the PDF.")
