import csv
import pandas as pd
import re
from decimal import Decimal
from datetime import datetime
from decimal import InvalidOperation

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
    if isinstance(amount_str, (int, float)):  # If it's already numeric
        return Decimal(amount_str)

    if not isinstance(amount_str, str) or not amount_str.strip():  # Handle None or empty strings
        return Decimal(0)

    try:
        # Remove currency symbols ($, €, £, etc.)
        amount_str = re.sub(r'[^\d,.-]', '', amount_str)

        # If it contains both '.' and ',', determine the format
        if '.' in amount_str and ',' in amount_str:
            if amount_str.rfind('.') > amount_str.rfind(','):
                # Case: "1,234.56" (US format) -> Remove comma (thousands separator)
                amount_str = amount_str.replace(',', '')
            else:
                # Case: "1.234,56" (European format) -> Remove dot, replace comma with dot
                amount_str = amount_str.replace('.', '').replace(',', '.')

        # If there are multiple dots or multiple commas, it's an invalid format
        elif amount_str.count('.') > 1 or amount_str.count(',') > 1:
            print(f"❗ Error parsing amount: {amount_str}, error: Invalid format")
            return Decimal(0)

        # Ensure comma is always replaced with dot before conversion
        amount_str = amount_str.replace(',', '.')

        return Decimal(amount_str)
    except (InvalidOperation, ValueError):
        print(f"❗ Error parsing amount: {amount_str}, error: Invalid format")
        return Decimal(0)  # Return 0 in case of parsing errors


def normalize_status(status):
    """
    Converts status to lowercase.
    """
    return status.lower()

from datetime import datetime

from datetime import datetime

from datetime import datetime

def normalize_date(date_str):
    """Converts various date formats into standard YYYY-MM-DD format."""
    if not isinstance(date_str, str) or not date_str.strip():
        return None  # Handle empty or non-string cases safely

    # Direct return if it's already in correct format
    if re.match(r"^\d{4}-\d{2}-\d{2}$", date_str):
        return date_str

    # List of possible date formats in the dataset
    date_formats = [
        "%Y-%m-%d",
        "%Y-%d-%m",  
        "%Y.%m.%d", 
        "%Y.%d.%m",
        "%Y/%m/%d", 
        "%Y/%d/%m", 
        "%d/%m/%Y",  
        "%m/%d/%Y",  
        "%d-%m-%Y",  
    ]

    for fmt in date_formats:
        try:
            return datetime.strptime(date_str, fmt).strftime("%Y-%m-%d")
        except ValueError:
            continue  # Try the next format

    # If all formats fail, print warning and return None
    print(f"❗ Warning: Unrecognized date format - {date_str}")
    return None



def process_row(row, headers):
    required_columns = {'transaction_date', 'description', 'amount', 'currency', 'status'}
    missing = required_columns - set(headers)
    
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    return {
        'transaction_date': normalize_date(row[headers.index('transaction_date')]),
        'description': row[headers.index('description')],
        'amount': parse_amount(row[headers.index('amount')]),
        'currency': row[headers.index('currency')],
        'status': normalize_status(row[headers.index('status')])
    }

    return normalized_data
    print("Headers:", headers)  
