import os
import pandas as pd
import csv
import json
from decimal import Decimal
from datetime import datetime
from utils import detect_delimiter, normalize_column_names, process_row  # type: ignore

def process_csv(file_path, has_headers=True):
    delimiter = detect_delimiter(file_path)
    
    with open(file_path, 'r', encoding='utf-8') as f:
        sample = f.read(1024)  # Read a sample to detect if there is a header
        detected_header = csv.Sniffer().has_header(sample)
    
    # Final decision on headers
    has_headers = has_headers if has_headers is not None else detected_header

    df = pd.read_csv(file_path, delimiter=delimiter, dtype=str, quotechar='"', skipinitialspace=True, header=0 if has_headers else None)

    # Handle files without headers
    if not has_headers:
        df.columns = ['transaction_date', 'description', 'amount', 'currency', 'status']
    else:
        df.columns = normalize_column_names(df.columns.tolist())

    # Debugging: Check column names
    print("Processed Headers:", df.columns.tolist())

    # Process and normalize data
    try:
        normalized_data = [process_row(row, df.columns.tolist()) for row in df.values]
    except ValueError as e:
        print(f"❗ Error processing CSV: {e}")
        return []

    return normalized_data

# Custom function to convert Decimal and datetime objects to JSON serializable format
def custom_json_serializer(obj):
    if isinstance(obj, Decimal):  
        return float(obj)  # Convert Decimal to float
    if isinstance(obj, datetime):  
        return obj.strftime("%Y-%m-%d")  # Convert datetime to string
    raise TypeError(f"Type {type(obj)} not serializable")

if __name__ == "__main__":
    input_file = "test_files/test1.csv"  # Change this for different test files
    results = process_csv(input_file)

    # Print processed output in JSON format
    print(json.dumps(results, indent=4, default=custom_json_serializer))