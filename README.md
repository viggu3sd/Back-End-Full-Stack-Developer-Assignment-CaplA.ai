README - CSV Normalization and Processing Script
Introduction
This Python script is designed to read CSV files with varying delimiters, normalize the data, and output it in a structured format. It correctly handles thousands separators in numbers, standardizes date formats, and ensures proper text formatting.

Features
✅ Automatic delimiter detection (,, ;, |, \t)
✅ Handles CSV files with or without headers
✅ Standardizes date format to YYYY-MM-DD
✅ Processes currency amounts correctly
✅ Supports quoted fields and special characters
✅ Outputs structured JSON data

Installation
Ensure you have Python 3.7+ installed. Then install dependencies using:

sh
Copy
Edit
pip install pandas
Usage
To run the script, specify the input file in main.py:

python
Copy
Edit
input_file = "test_files/test1.csv"  # Update with your test file
Then execute:

sh
Copy
Edit
python main.py
Expected Output Format
json
Copy
Edit
[
    {
        "transaction_date": "2024-01-15",
        "description": "Office Supplies",
        "amount": 1234.56,
        "currency": "USD",
        "status": "completed"
    }
]
File Structure
php
Copy
Edit
📂 Project Directory
│── main.py               # Main script to process CSV files
│── utils.py              # Helper functions for normalization
│── test_files/           # Sample test files
│── README.md             # Documentation
│── report.md             # Detailed implementation report
Contributing
If you'd like to improve this script, feel free to submit a pull request.
