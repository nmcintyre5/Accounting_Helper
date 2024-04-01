import pandas as pd

def main():
    try:
        # Prompt the user for the filename
        filename = input("Enter the file path to read in: ")

        # Read the dataset from the CSV file
        df = pd.read_csv(filename)

        # Check for rows with blank Tax Category
        blank_tax_category_rows = df[df['Tax Category'].isnull()]

        # If there are rows with blank Tax Category, prompt the user to manually input the tax category
        if not blank_tax_category_rows.empty:
            # List of available tax categories
            tax_categories = [
                "Advertising", "Car Repair", "Charity", "Coaching/Educational",
                "Credential Renewal", "Entertainment", "Equipment Rentals",
                "Equipment Repairs", "Gas", "Interest", "Legal & Professional",
                "Meals", "Medical", "Meetings", "Office expense", "Parking",
                "Professional Memberships & Dues", "Professional Research",
                "Promotional", "Supplies", "Telephone", "Trade Publications",
                "Travel", "Web Subscriptions"
            ]

            # Display the list of tax categories with corresponding numbers
            print("Select the tax category for each transaction by entering the corresponding number:")
            for i, category in enumerate(tax_categories, start=1):
                print(f"{i}. {category}")

            for index, row in blank_tax_category_rows.iterrows():
                while True:
                    user_input = input(f"Enter the number corresponding to the tax category for the transaction:\n'{row['Description']} \nAmount: {row['Amount']}: ")
                    try:
                        selected_category_index = int(user_input)
                        if 1 <= selected_category_index <= len(tax_categories):
                            df.loc[index, 'Tax Category'] = tax_categories[selected_category_index - 1]
                            break
                        else:
                            print("Invalid number. Please enter a valid number from the list.")
                    except ValueError:
                        print("Invalid input. Please enter a number.")

        # Check for rows with blank GIG
        blank_gig_category_rows = df[df['GIG'].isnull()]

        # If there are rows with blank GIG, prompt the user to manually input the gig category
        if not blank_gig_category_rows.empty:
            # List of available gig categories
            gig_categories = [
                "RE", "Tutoring", "Dog Sitting", "General",
                "Personal"
            ]

            # Display the list of gig categories with corresponding numbers
            print("Select the gig category for each transaction by entering the corresponding number:")
            for i, category in enumerate(gig_categories, start=1):
                print(f"{i}. {category}")

            for index, row in blank_gig_category_rows.iterrows():
                while True:
                    user_input = input(f"Enter the number corresponding to the gig category for the transaction:\n'{row['Description']} \nAmount: {row['Amount']}: ")
                    try:
                        selected_category_index = int(user_input)
                        if 1 <= selected_category_index <= len(gig_categories):
                            df.loc[index, 'GIG'] = gig_categories[selected_category_index - 1]
                            break
                        else:
                            print("Invalid number. Please enter a valid number from the list.")
                    except ValueError:
                        print("Invalid input. Please enter a number.")
        
        # Sort the DataFrame in ascending order by 'Tax Category'
        df.sort_values(by='Tax Category', inplace=True)

        # Sort the DataFrame in ascending order by 'GIG'
        df.sort_values(by='GIG', inplace=True)

        # Define the output filename by adding "_mod" to the end of the input filename
        output_filename = filename.replace('.csv', '_mod.csv')

        # Export the modified data to a new CSV file
        df.to_csv(output_filename, index=False)

        print(f"Data has been exported to: {output_filename}")

    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
