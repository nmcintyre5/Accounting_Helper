import pandas as pd

def select_bank():
    print("Select the bank from which you exported the data:")
    print("1. AMEX")
    print("2. Discover")
    print("3. Chase")
    print("4. Citi") 
    while True:
        choice = input("Enter the number corresponding to your choice: ")
        if choice in ['1', '2', '3','4']:
            if choice == '1':
                return 'AMEX'
            elif choice == '2':
                return 'Discover'
            elif choice == '3':
                return 'Chase'
            elif choice == '4':
                return 'Citi'
        else:
            print("Invalid input. Please enter a valid number.")

def process_file(filename, selected_bank):
    # Read the dataset from the CSV file
    df = pd.read_csv(filename)

    if selected_bank == 'AMEX':
        # For AMEX:
        
        # Filter out rows with negative amounts
        df = df[df['Amount'] >= 0]

        # Define the columns needed for further analysis
        columns_of_interest = ['Date', 'Amount', 'Extended Details', 'Category']

        # Select only the desired columns
        df = df[columns_of_interest]

        # Rename the 'Extended Details' column to 'Description' for clarity
        df.rename(columns={'Extended Details': 'Description'}, inplace=True)

        # Reorder columns to match the desired spreadsheet layout
        df = df[['Date', 'Description', 'Amount', 'Category']]

        # Append additional columns required for data processing
        df['Tax Category'] = ''
        df['Source'] = 'AMEX'
        df['GIG'] = 'Tutoring'

        # Define a function to update 'Tax Category' based on 'Category' contents, 
        # and if not categorized, based on 'Description' contents
        def update_tax_category(category, description):
            if 'Restaurant' in category:
                return 'Meals'
            elif 'Supplies' in category:
                return 'Supplies'
            elif 'Travel' in category:
                return 'Travel'
            elif 'Transportation' in category:
                return 'Travel'
            elif 'Parking' in category:
                return 'Parking'
            elif 'Health Care Services' in category:
                return 'Medical'
            elif 'Entertainment' in category:
                return 'Entertainment'
            elif 'NYTimes.com' in description:
                return 'Trade Publications'
            elif 'DMV' in description:
                return 'Legal & Professional'
            elif 'ZOOM.US' in description:
                return 'Web Subscriptions'
            elif 'PARKING' in description:
                return 'Parking'
            elif 'WALMART.COM' in description:
                return 'Web Subscriptions'
            elif 'INSURANCE' in description:
                return 'Insurance'
            else:
                return ''

        # Apply the update_tax_category_description function to the 'Description' column to further populate 'Tax Category'
        df['Tax Category'] = df.apply(lambda row: update_tax_category(row['Category'], row['Description']), axis=1)

        # Modify 'GIG' column based on 'Tax Category'
        def update_gig(tax_category, gig):
            if tax_category == 'Car Insurance':
                return 'General'
            elif tax_category == 'Medical':
                return 'General'
            else:
                return gig

        # Apply the update_gig function to the 'GIG' column
        df['GIG'] = df.apply(lambda row: update_gig(row['Tax Category'], row['GIG']), axis=1)


    elif selected_bank == 'Discover':
        # For Discover:
        # Filter out rows with negative amounts
        df = df[df['Amount'] >= 0]

        # Define the columns needed for further analysis
        columns_of_interest = ['Post Date', 'Description', 'Amount', 'Category']

        # Select only the desired columns
        df = df[columns_of_interest]

        # Rename the 'Extended Details' column to 'Description' for clarity
        df.rename(columns={'Post Date': 'Date'}, inplace=True)

        # Reorder columns to match the desired spreadsheet layout
        df = df[['Date', 'Description', 'Amount', 'Category']]

        # Append additional columns required for data processing
        df['Tax Category'] = ''
        df['Source'] = 'Discover'
        df['GIG'] = 'Personal'

        # Define a function to update 'Tax Category' based on 'Category' contents, 
        # and if not categorized, based on 'Description' contents
        def update_tax_category(category, description):
            if 'Supermarkets' in category:
                return 'Meals'
            elif 'Restaurants' in category:
                return 'Meals'
            elif 'Medical Services' in category:
                return 'Medical'
            elif 'Merchandise' in category:
                return 'Supplies'
            elif 'Services' in category:
                return 'Services'
            elif 'TARGET' in description:
                return 'Supplies'
            else:
                return ''

        # Apply the update_tax_category_description function to the 'Description' column to further populate 'Tax Category'
        df['Tax Category'] = df.apply(lambda row: update_tax_category(row['Category'], row['Description']), axis=1)

    elif selected_bank == 'Chase':
        # For Chase:
        # Filter out rows with negative amounts
        df = df[df['Amount'] <= 0]

        # Multiply 'Amount' column by -1
        df['Amount'] = df['Amount'].multiply(-1)

        # Define the columns needed for further analysis
        columns_of_interest = ['Post Date', 'Description', 'Category', 'Amount']

        # Select only the desired columns
        df = df[columns_of_interest]

        # Rename the 'Extended Details' column to 'Description' for clarity
        df.rename(columns={'Post Date': 'Date'}, inplace=True)

        # Reorder columns to match the desired spreadsheet layout
        df = df[['Date', 'Description', 'Amount', 'Category']]

        # Append additional columns required for data processing
        df['Tax Category'] = ''
        df['Source'] = 'Chase'
        df['GIG'] = 'Personal'

        # Define a function to update 'Tax Category' based on 'Category' contents, 
        # and if not categorized, based on 'Description' contents
        def update_tax_category(category, description):
            if 'Groceries' in category:
                return 'Meals'
            elif 'Shopping' in category:
                return 'Supplies'
            else:
                return ''

        # Apply the update_tax_category_description function to the 'Description' column to further populate 'Tax Category'
        df['Tax Category'] = df.apply(lambda row: update_tax_category(row['Category'], row['Description']), axis=1)

    elif selected_bank == 'Citi':
        # For Citi:

        # Define the columns needed for further analysis
        columns_of_interest = ['Date', 'Description', 'Debit']

        # Select only the desired columns
        df = df[columns_of_interest]

        # Rename the 'Extended Details' column to 'Description' for clarity
        df.rename(columns={'Debit': 'Amount'}, inplace=True)

        # Add an empty 'Category' column
        df['Category'] = ''

        # Reorder columns to match the desired spreadsheet layout
        df = df[['Date', 'Description', 'Amount', 'Category']]

        # Drop rows with null values in the 'Amount' column
        df = df.dropna(subset=['Amount'])

        # Append additional columns required for data processing
        df['Tax Category'] = ''
        df['Source'] = 'Citi'
        df['GIG'] = 'General'

        # Define a function to update 'Tax Category' based on 'Description' contents
        def update_tax_category(description):
            if 'COSTCO GAS' in description:
                return 'Gas'
            else:
                return 'Supplies'

        # Apply the update_tax_category_description function to the 'Description' column to further populate 'Tax Category'
        df['Tax Category'] = df.apply(lambda row: update_tax_category(row['Description']), axis=1)

        # Modify 'GIG' column based on 'Tax Category'
        def update_gig(tax_category, gig):
            if tax_category == 'Gas':
                return 'General'
            else:
                return 'Personal'

        # Apply the update_gig function to the 'GIG' column
        df['GIG'] = df.apply(lambda row: update_gig(row['Tax Category'], row['GIG']), axis=1)


    return df

def export_to_csv(df):
    output_filename = "accounting_mod.csv"
    df.to_csv(output_filename, index=False)
    print(f"Data has been exported to: {output_filename}")

def main():
    all_data_frames = []  # List to store all data frames

    while True:
        filepath = input("Enter the file path to read in (or type 'done' to finish): ")
        if filepath.lower() == 'done':
            break
        selected_bank = select_bank()
        df = process_file(filepath, selected_bank)
        all_data_frames.append(df)  # Append the processed DataFrame to the list

    # Concatenate all data frames into one
    final_df = pd.concat(all_data_frames, ignore_index=True)
    export_to_csv(final_df)

if __name__ == "__main__":
    main()
