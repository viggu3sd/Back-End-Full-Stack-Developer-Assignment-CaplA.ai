import os
import pandas as pd
import csv
import json
from decimal import Decimal  # Fix: Import Decimal
from datetime import datetime  # Fix: Import datetime if needed
from utils import detect_delimiter, normalize_column_names, process_row  # type: ignore

def process_csv(file_path, has_headers=True):
    delimiter = detect_delimiter(file_path)
    
    with open(file_path, 'r', encoding='utf-8') as f:
        sample = f.read(1024)  # Read a sample to detect if there is a header
        has_headers = csv.Sniffer().has_header(sample) if has_headers else False
    
    df = pd.read_csv(file_path, delimiter=delimiter, dtype=str, quotechar='"', skipinitialspace=True)

    # Handle files without headers
    if not has_headers:
        column_mapping = {
            0: 'transaction_date',
            1: 'description',
            2: 'amount',
            3: 'currency',
            4: 'status'
        }
        df.rename(columns=column_mapping, inplace=True)
    else:
        df.columns = normalize_column_names(df.columns)

    # Process and normalize data
    normalized_data = [process_row(row, df.columns.tolist()) for row in df.values]

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




# if __name__ == "__main__":
#     input_file = "test_files/no_header.csv"  # No headers file
#     results = process_csv(input_file, has_headers=False)

#     for row in results:
#         print(row)

