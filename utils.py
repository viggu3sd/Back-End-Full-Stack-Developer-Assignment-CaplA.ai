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
    Convert column names to snake_case and remove special characters.
    """
    return [re.sub(r'[^a-zA-Z0-9]', '_', col).strip().lower() for col in columns]

def parse_amount(amount_str):
    """
    Converts amount strings to Decimal format.
    Handles both '1,234.56' and '1.234,56' formats.
    """
    amount_str = amount_str.replace(',', '') if '.' in amount_str else amount_str.replace('.', '').replace(',', '.')
    return Decimal(amount_str)

def normalize_status(status):
    """
    Converts status to lowercase.
    """
    return status.lower()

def normalize_date(date_str):
    """
    Converts various date formats to standard YYYY-MM-DD.
    """
    return datetime.strptime(date_str, "%Y-%m-%d")

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
