import csv
import pandas as pd
import re
from decimal import Decimal
from datetime import datetime

def detect_delimiter(file_path):
    """
    Detects the delimiter in a CSV file by checking the most frequent separator.
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        first_line = f.readline()
    delimiters = [',', ';', '|', '\t']
    delimiter_counts = {d: first_line.count(d) for d in delimiters}
    return max(delimiter_counts, key=delimiter_counts.get)  # Return delimiter with max occurrences

def normalize_column_names(columns):
    """
    Convert column names to snake_case, remove special characters, and handle currency in amount columns.
    """
    normalized = [re.sub(r'[^a-zA-Z0-9]', '_', col).strip().lower() for col in columns]
    
    # Ensure 'amount' column is correctly identified
    normalized = ['amount' if 'amount' in col else col for col in normalized]
    
    return normalized


from decimal import Decimal

def parse_amount(amount_str):
    """Parses and normalizes amount values safely."""
    if isinstance(amount_str, (float, int)):  # Check if it's already a number
        amount_str = f"{amount_str}"  # Convert it to a string safely

    # Handle different number formats (e.g., "1,234.56" or "1.234,56")
    amount_str = amount_str.replace(',', '') if '.' in amount_str else amount_str.replace('.', '').replace(',', '.')

    try:
        return Decimal(amount_str)  # Convert to Decimal for precision
    except Exception as e:
        print(f"Error parsing amount: {amount_str}, error: {e}")
        return Decimal(0)  # Default to 0 if parsing fails



def normalize_status(status):
    """
    Converts status to lowercase.
    """
    return status.lower()

from datetime import datetime

from datetime import datetime

def normalize_date(date_str):
    """Converts various date formats into standard YYYY-MM-DD format."""
    if not isinstance(date_str, str):
        return None  # Handle empty or non-string cases safely

    # List of possible date formats in the dataset
    date_formats = ["%Y-%m-%d", "%d/%m/%Y", "%m/%d/%Y", "%d-%m-%Y"]

    for fmt in date_formats:
        try:
            return datetime.strptime(date_str, fmt).strftime("%Y-%m-%d")
        except ValueError:
            continue  # Try the next format

    # If all formats fail, return None or raise an error
    print(f"❗ Warning: Unrecognized date format - {date_str}")
    return None




def process_row(row, headers):
    """
    Processes a single row of data and normalizes it.
    """
    normalized_data = {
        'transaction_date': normalize_date(row[headers.index('transaction_date')]),
        'description': row[headers.index('description')],
        'amount': parse_amount(row[headers.index('amount')]),
        'currency': row[headers.index('currency')],
        'status': normalize_status(row[headers.index('status')])
    }
    return normalized_data
    print("Headers:", headers)  # Debugging line
