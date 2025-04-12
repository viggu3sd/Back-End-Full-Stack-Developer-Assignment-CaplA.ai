# **CSV Normalization and Processing Script**

## **Introduction**
This Python script is designed to **read CSV files with varying delimiters**, normalize the data, and output it in a structured format. It correctly handles **thousands separators in numbers**, **standardizes date formats**, and ensures **proper text formatting**.

## **Features**
✅ **Automatic delimiter detection** (`,`, `;`, `|`, `\t`)
✅ **Handles CSV files with or without headers**  
✅ **Standardizes date format to `YYYY-MM-DD`**  
✅ **Processes currency amounts correctly**  
✅ **Supports quoted fields and special characters**  
✅ **Outputs structured JSON data**  

## **Installation**
Ensure you have **Python 3.7+** installed. Then install dependencies using:  
```sh
pip install pandas
```

## **Usage**
To run the script, specify the input file in `main.py`:
```python
input_file = "test_files/test1.csv"  # Update with your test file
```
Then execute:
```sh
python main.py
```

## **Expected Output Format**
```json
[
    {
        "transaction_date": "2024-01-15",
        "description": "Office Supplies",
        "amount": 1234.56,
        "currency": "USD",
        "status": "completed"
    }
]
```

## **File Structure**
```
📂 Project Directory
│── main.py               # Main script to process CSV files
│── utils.py              # Helper functions for normalization
│── test_files/           # Sample test files
│── README.md             # Documentation
│── report.md             # Detailed implementation report
```

## **Supported Data Normalization**
- **Column Name Normalization:** Converts to `snake_case` (e.g., `Transaction_Date` → `transaction_date`).
- **Date Standardization:** Supports multiple date formats and converts to `YYYY-MM-DD`.
- **Numeric Handling:** Handles different formats (e.g., `$1,234.56` → `1234.56`, `1.234,56` → `1234.56`).
- **Status Normalization:** Converts status values to lowercase (`COMPLETED` → `completed`).

## **Handling Special Cases**
### **1. Automatic Delimiter Detection**
The script detects the correct delimiter dynamically, supporting:
- Comma (`,`) - **test1.csv**
- Semicolon (`;`) - **test2.csv**
- Pipe (`|`) - **test3.csv**

### **2. Handling CSV Files Without Headers**
If a file does not have headers, the script assigns:
```python
{
    0: 'transaction_date',
    1: 'description',
    2: 'amount',
    3: 'currency',
    4: 'status'
}
```

## **Contributing**
If you'd like to improve this script, feel free to submit a **pull request**. **Lets Build**

## **License**
This project is **free to use** for educational purposes.
