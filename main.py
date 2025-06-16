from read import load_data
from write import update_database
from operations import display_products, option_1, option_2, option_3

def display_intro():
    """Displays a welcome message to the system administrator."""
    print("WeCare Wholesale.")
    print("Welcome system admin")

def admin_options(products, database_name):
    """
    Displays the main admin menu and handles user selection.

    Args:
        products (list): The current product list.
        database_name (str): The name of the product database file.
    """
    main_loop = True
    while main_loop:
        try:
            # Display menu options
            print("-" * 50)
            print("Given below are options for carrying out operations")
            print("-" * 50)
            print("\n")
            print("Press 1 to sell product to customer")
            print("Press 2 to purchase from manufacturer")
            print("Press 3 to exit from system")
            print("\n")
            print("-" * 50)
            print("\n")

            # Get user choice
            option = input("Enter option: ")
            print("\n")
            while not option.isnumeric():
                print("Input should be a number")
                option = input("Enter option: ")
                print("\n")

            # Process user choice
            if option == "1":
                option_1(products, database_name)  # Sell products
            elif option == "2":
                option_2(products, database_name)  # Restock products
            elif option == "3":
                option_3()  # Exit system
                main_loop = False
            else:
                print("Please enter option 1,2 or 3")
                print("\n")
        except Exception as e:
            # Handle errors in menu navigation
            print(f"An error occurred in menu navigation: {e}")
            print("Returning to main menu...\n")

def main():
    """Main function, entry point of the program."""
    try:
        # Initialize system
        display_intro()
        database_name = "product_database.txt"
        
        # Load product data
        products = load_data(database_name)
        
        # Display products and show menu
        display_products(products)
        admin_options(products, database_name)
    except Exception as e:
        # Handle critical errors
        print(f"A critical error occurred: {e}")
        print("The program will now exit.")

if __name__ == "__main__":
    main()
