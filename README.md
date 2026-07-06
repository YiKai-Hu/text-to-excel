Text to Excel Converter



A simple Python tool for converting plain text lists (with index and name) into a clean Excel spreadsheet.

&#x20;Features



Automatically extracts serial numbers and names from each line.

Handles various separators: spaces, tabs, dots, Chinese punctuation, or even no separator (e.g., `1张三`).

Outputs a standard `.xlsx` file with proper column headers.

Skips empty lines and reports format errors for problematic rows.



How It Works



Place your text file (e.g., `sample\_data.txt`) in the same folder as the script.

The script reads the file line by line.

It extracts the first number it finds as the index, and treats the rest as the name.

Saves the result as an Excel file on your desktop.



Requirements



Python 3.7 or higher

Required libraries: `pandas`, `openpyxl`



Installation

Open your terminal (CMD) and run:

```bash

py -m pip install pandas openpyxl

