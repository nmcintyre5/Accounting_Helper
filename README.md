# Accounting Helper Project

[Overview](#overview) | [Key Features](#key-features) | [How To Use](#how-to-use)

## Overview
This Python script enables users to process financial data exported from various banks and categorize transactions for tax purposes based on predefined categorization rules for transactions. Supported banks include: AMEX, Discover, Chase, and Citi. 

## Key Features

- **Data Processing**: The script processes financial data exported as a .csv file from different banks (AMEX, Discover, Chase, and/or Citi)

    Note: Ensure that the financial data files are in CSV format and adhere to the expected structure for accurate processing. It's recommended to export the data directly from your bank without any modifications before running the script.

- **Supported Tax Categories**: The script allows the user to categorize transactions into one of the following tax categories:

    - Advertising
    - Car Repair
    - Charity
    - Coaching/Educational
    - Credential Renewal
    - Entertainment
    - Equipment Rentals
    - Equipment Repairs
    - Gas
    - Interest
    - Legal & Professional
    - Meals
    - Medical
    - Meetings
    - Office expense
    - Parking
    - Professional Memberships & Dues
    - Professional Research
    - Promotional
    - Supplies
    - Telephone
    - Trade Publications
    - Travel
    - Web Subscriptions

- **Predefined Categorization Rules for Transactions**: Transactions are automatically categorized for tax purposes based on predefined criteria, such as description and category.

    AMEX categorization rules:
    - If the category contains "Restaurant", the expense is categorized as Meals for tax purposes.
    - If the category contains "Parking", the expense is categorized as Parking for tax purposes.
    - If the category contains "Supplies", the expense is categorized as Supplies for tax purposes.
    - If the description contains "NYTimes.com", the expense is categorized as Trade Publications for tax purposes.
    - If the description contains "DMV", the expense is categorized as Legal & Professional for tax purposes.
    - If the description contains "ZOOM.US", the expense is categorized as Web Subscriptions for tax purposes.
    - If the description contains "PARKING", the expense is categorized as Parking for tax purposes.
    - If the description contains "WALMART.COM", the expense is categorized as Web Subscriptions for tax purposes.

    Discover categorization rules:
    - If the category contains Supermarkets or Restaurants, the expense is categorized as Meals for tax purposes.
    - If the category contains Medical Services, the expense is categorized as Medical for tax purposes.
    - If the category contains Merchandise, the expense is categorized as Supplies for tax purposes.
    - If the category contains Services, the expense is categorized as Services for tax purposes.
    - If the description contains TARGET, the expense is categorized as Supplies for tax purposes.

    Chase categorization rules:
    - If the category contains Groceries, the expense is categorized as Meals for tax purposes.
    - If the category contains Shopping, the expense is categorized as Supplies for tax purposes.

    Citi categorization rules:
    - If the description contains COSTCO GAS, the expense is categorized as Gas for tax purposes.
    - Otherwise, the expense is categorized as Supplies for tax purposes.

- **Export to CSV**: The processed data is exported to a CSV file with detailed columns (see below). It will be saved in the same directory where the Python script is executed.

    Columns in the exported CSV file:
    - Date: Date of the transaction
    - Description: Description of the transaction
    - Amount: Amount of the transaction
    - Category: Category of the transaction
    - Tax Category: Tax category assigned to the transaction
    - Source: Source bank of the transaction
    - GIG: Category assigned to the transaction (useful for those with multiple revenue streams)

- **Interactive Interface**: Users can interactively select the bank and provide file paths for processing.
- **Optional Tax and Gig Categorizer Script**: This script facilitates interactive processing and modification of accounting data stored in CSV format, complementing the "Accounting Helper" script. It prompts the user to input the file path of the CSV file containing accounting data "accounting_mod.csv". The script reads the data into a pandas DataFrame, checks for blank values in the 'Tax Category' and 'GIG' columns, prompts the user to input missing tax and gig categories, sorts the DataFrame, and exports the modified data to a new CSV file with "_mod.csv" appended to the file name.


## How To Use

### Prerequisites

1. **Python 3**: Ensure you have Python 3 installed on your system.
2. **Dependencies**: Pandas library is required for running the script. If you haven't installed it yet, you can do so using pip:
    ```bash
    pip install pandas
    ```

### Running the Script

1. **Clone Repository**: Clone the repository containing the script.
2. **Navigate to Directory**: Open terminal and navigate to the directory containing the script.
3. **Run Accounting Helper Script**: Execute the script by running:
    ```bash
    python3 accounting_helper.py
    ```
4. **Follow Instructions**: Provide the file path of the financial data exported from your bank and select the bank.
    ![Screenshot of the Accounting Helper scipt running](/Accounting_Helper_Run.png)
5. **Exported Data**: Once processed, the modified data will be exported to a CSV file named "accounting_mod.csv" in your Documents folder.
    Note: The transaction data shown below has been whited out for privacy purposes. 
    ![Screenshot of the exported data](/Modified_Data_Blanked.png)
6. **Optional Step**: Run Tax and Gig Categorize Script: After exporting the CSV file, optionally run the Tax and Gig Categorizer script to categorize transactions with blank tax and gig categories. 
    - **Execution**: Execute the script by running:
      ```bash
      python3 tax_and_gig_categorizer.py
      ```
    - **Follow Instructions**: Follow the on-screen instructions to categorize transactions with blank tax and gig categories.
        ![Screenshot of the Tax and Gig Categorizer script running](/Tax_and_Gig_Categorizer_Run.png)


