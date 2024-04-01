# Account Helper Project

This Python script enables users to process financial data exported from various banks and categorize transactions for tax purposes based on predefined criteria. Supported banks include AMEX, Discover, Chase, and Citi.

## Features

- **Data Processing**: The script processes financial data exported from different banks.
- **Categorization**: Transactions are categorized for tax purposes based on predefined criteria such as description and category.
- **Export to CSV**: The processed data is exported to a CSV file with detailed columns.
- **Interactive Interface**: Users can interactively select the bank and provide file paths for processing.

## Usage

### Prerequisites

1. **Python 3**: Ensure you have Python 3 installed on your system.
2. **Dependencies**: Pandas library is required for running the script. If you haven't installed it yet, you can do so using pip:
### `pip install pandas`


### Running the Script

1. **Clone Repository**: Clone the repository containing the script.
2. **Navigate to Directory**: Open terminal and navigate to the directory containing the script.
3. **Run Accounting Helper Script**: Execute the script by running:
### `python3 accounting_helper.py`
4. **Follow Instructions**: Provide the file path of the financial data exported from your bank and select the bank.
5. **Exported Data**: Once processed, the modified data will be exported to a CSV file named "accounting_mod.csv" in your Documents folder.

### Optional: Additional Step

After exporting the CSV file, optionally run the Tax and Gig Categorizer script to categorize transactions with blank tax and gig categories. 

#### Tax and Gig Categorizer Script

1. **Run Script**: Execute the script by running:
### `python3 tax_and_gig_categorizer.py`

2. **Follow Instructions**: Follow the on-screen instructions to categorize transactions with blank tax and gig categories.

### Note

Ensure that the financial data files are in CSV format and adhere to the expected structure for accurate processing. It's recommended to export the data directly from your bank without any modifications before running the script.

This script facilitates interactive processing and modification of accounting data stored in CSV format, complementing the "Accounting Helper" script. It prompts the user to input the file path of the CSV file containing accounting data processed by another program. The script reads the data into a pandas DataFrame, checks for blank values in the 'Tax Category' and 'GIG' columns, prompts the user to input missing tax and gig categories, sorts the DataFrame, and exports the modified data to a new CSV file.

## Columns in the Exported CSV File

- Date: Date of the transaction
- Description: Description of the transaction
- Amount: Amount of the transaction
- Category: Category of the transaction
- Tax Category: Tax category assigned to the transaction
- Source: Source bank of the transaction
- GIG: Category assigned to the transaction (useful for businesses with multiple categories)

## Functions

- `select_bank()`: Allows users to select the bank from which the data was exported.
- `process_file(filename, selected_bank)`: Processes the financial data based on the selected bank.
- `export_to_csv(df)`: Exports the processed data to a CSV file named "accounting_mod.csv".
- `main()`: Controls the main flow of the script, prompting users for file paths and bank selection.


