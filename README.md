# Account Helper Project

This script allows users to process financial data exported from various banks and categorize transactions based on predefined criteria. The supported banks include AMEX, Discover, Chase, and Citi.

The final exported CSV file will have the following columns:
- Date: Date of the transaction
- Description: Description of the transaction
- Amount: Amount of the transaction
- Category: Category of the transaction
- Tax Category: Tax category based on predefined criteria
- Source: Source bank of the transaction
- GIG: Additional categorization helpful for managing multiple businesses, such as photography or consulting.

## How to run the project locally:
Step 1: Install the latest Python3 in MacOS
Step 2: Check if pip3 and python3 are correctly installed.
### `python3 --version`
### `pip3 --version`
Step 3: Upgrade your pip to avoid errors during installation.
### `pip3 install --upgrade pip`
Step 4: Enter the following command to install Pandas using pip3.
### `pip3 install pandas`
Step 5: Open terminal and run the Accounting Helper
### `python3 Accounting_Helper.py`
Step 6: FINISH THIS WITH FILE PAHT EXPORT AND EXPLAIN that you may then read it into tax and gig categorizer program

## Functions:
- `select_bank()`: Allows users to select the bank from which the data was exported.
- `process_file(filename, selected_bank)`: Processes the financial data based on the selected bank.
- `export_to_csv(df)`: Exports the processed data to a CSV file named "accounting_mod.csv".
- `main()`: Controls the main flow of the script, prompting users for file paths and bank selection.

To use the script, users need to provide the file path of the financial data exported from their bank. The script will then guide users through the process of categorizing transactions and export the modified data to a CSV file.

**Note:** Ensure the financial data files are in CSV format and follow the expected structure for accurate processing.

---

This script allows the user to interactively process and modify accounting data stored in CSV format, complementing the "Accounting Helper" script. It prompts the user to input the file path of the CSV file containing accounting data processed by another program. The script reads the data into a pandas DataFrame, checks for blank values in the 'Tax Category' and 'GIG' columns, prompts the user to input missing tax and gig categories, sorts the DataFrame, and exports the modified data to a new CSV file.

**Columns in the final exported CSV file:**
- Date: Date of the transaction
- Description: Description of the transaction
- Amount: Amount of the transaction
- Category: Category of the transaction
- Tax Category: Tax category assigned to the transaction
- Source: Source bank of the transaction
- GIG: Category assigned to the transaction (useful for businesses with multiple categories)
