import datetime
from write import generate_invoice, generate_purchase_invoice, update_database

def display_products(products):
    """
    Displays a formatted table of all available products.
    
    Args:
        products (list): List of product dictionaries to display.
    """
    # Print table header
    print("\nAvailable Products:")
    print("-" * 150)
    headers = ["ID", "PRODUCT NAME", "BRAND NAME", "QUANTITY", "COST PRICE", "ORIGIN COUNTRY"]
    format_str = "{:<5} {:<25} {:<25} {:<15} {:<15} {:<15}"
    print(format_str.format(*headers))
    print("-" * 150)
    
    # Print each product row
    for product in products:
        print(format_str.format(
            product["id"],
            product["name"],
            product["brand"],
            product["stock"],
            product["cost_price"],
            product["country"]
        ))
    print("-" * 150)
    print("\n")

def option_1(products, database_name):
    """
    Handles the product selling process and invoice generation.

    Args:
        products (list): The current product list.
        database_name (str): The name of the product database file.
    """
    try:
        # Get customer information
        print("-" * 50)
        print("Enter customer details for bill generation")
        print("-" * 50)
        print("\n")

        customer_name = input("Enter name of customer: ")
        phone_number = input("Enter phone number of customer: ")
        # Validate phone number
        while not phone_number.isnumeric():
            print("\nInvalid number. Please enter again")
            phone_number = input("Enter phone number of customer: ")

        print("-" * 50)
        print("\n")

        # Initialize sales variables
        item_selling = []
        grand_total = 0
        sell_loop = True
        free_items = 0
        total_quantity = 0

        display_products(products)

        # Product selection loop
        while sell_loop:
            try:
                print("\n")
                # Get product ID
                product_id = input("Enter the ID of the product you want to sell: ")
                while not product_id.isnumeric() or int(product_id) > len(products) - 1:
                    print("Invalid ID")
                    product_id = input("Enter the ID of the product you want to sell: ")
                    print("\n")
                product_id = int(product_id)

                # Get product quantity
                product_quantity = input("Enter the quantity of product: ")
                print("\n")
                while not product_quantity.isnumeric():
                    print("Invalid Quantity")
                    product_quantity = input("Enter the quantity of product: ")
                    print("\n")

                # Apply promotion: Buy 3, Get 1 Free
                free_items = int(product_quantity) // 3
                total_quantity = int(product_quantity) + free_items

                # Check stock availability
                while (
                    int(product_quantity) <= 0 or products[product_id]["stock"] < total_quantity
                ):
                    print("THE QUANTITY YOU ARE LOOKING FOR IS UNAVAILABLE\n")
                    product_quantity = input("Enter the quantity of product: ")
                    if product_quantity.isnumeric():
                        free_items = int(product_quantity) // 3
                        total_quantity = int(product_quantity) + free_items
                    else:
                        while not product_quantity.isnumeric():
                            print("Invalid Quantity")
                            product_quantity = input("Enter the quantity of product: ")
                            print("\n")

                product_quantity = int(product_quantity)
                print("You have received ", free_items, " free items")

                # Update stock quantity
                products[product_id]["stock"] -= total_quantity

                # Calculate price (markup is 2x cost)
                individual_item_price = products[product_id]["cost_price"] * 2
                total_item_price = individual_item_price * product_quantity
                grand_total += total_item_price

                # Add item to sales list
                item_selling.append(
                    {
                        "name": products[product_id]["name"],
                        "brand": products[product_id]["brand"],
                        "product_quantity": product_quantity,
                        "total_quantity": total_quantity,
                        "individual_item_price": individual_item_price,
                        "total_item_price": total_item_price,
                    }
                )

                print("\n" + "-" * 50)
                display_products(products)

                # Check if more products to sell
                decision = input("Are there more products to sell?(y/n): ").lower()
                while not decision == "y" and not decision == "n":
                    print("Invalid input")
                    decision = input("Are there more products to sell?(y/n): ").lower()
                if decision == "n":
                    sell_loop = False
                else:
                    display_products(products)
            except Exception as e:
                # Handle errors in sale process
                print(f"Error processing sale: {e}")
                print("Please try again\n")

        # Generate invoice and update database
        generate_invoice(customer_name, phone_number, item_selling, grand_total)
        update_database(products, database_name)
    except Exception as e:
        # Catch all other exceptions
        print(f"An error occurred during sales process: {e}")
        print("Returning to main menu...\n")

def option_2(products, database_name):
    """
    Handles the restocking of products from a vendor.

    Args:
        products (list): The current product list.
        database_name (str): The name of the product database file.
    """
    try:
        # Begin restocking process
        print("-" * 50)
        print("RESTOCKING IN PROGRESS")
        print("-" * 50)
        print("\n")

        # Get vendor name
        vendor_name = input("Enter name of vendor: ")
        restock_loop = True
        display_products(products)

        # Initialize restocking variables
        restock_items = []
        grand_total_cost = 0

        # Product selection loop
        while restock_loop:
            try:
                # Get product ID
                product_id = input("Enter ID of product you want to restock: ")
                while not product_id.isnumeric() or int(product_id) > len(products) - 1:
                    print("Invalid ID")
                    product_id = input("Enter ID of product you want to restock: ")
                    print("\n")
                product_id = int(product_id)

                # Get product quantity
                product_quantity = input("Enter QUANTITY of product you want to restock: ")
                while not product_quantity.isnumeric():
                    print("Invalid Quantity")
                    product_quantity = input("Enter QUANTITY of product you want to restock: ")
                    print("\n")

                product_quantity = int(product_quantity)
                print("\n")

                # Update stock
                products[product_id]["stock"] += product_quantity

                # Calculate cost
                total_item_cost = product_quantity * products[product_id]["cost_price"]
                grand_total_cost += total_item_cost

                # Add item to restock list
                restock_items.append(
                    {
                        "name": products[product_id]["name"],
                        "brand": products[product_id]["brand"],
                        "product_quantity": product_quantity,
                        "cost_price": products[product_id]["cost_price"],
                        "total_item_cost": total_item_cost,
                    }
                )

                display_products(products)

                # Check if more products to restock
                decision = input("Are there more products to purchase?(y/n): ").lower()
                while not decision == "y" and not decision == "n":
                    print("Invalid input")
                    decision = input("Are there more products to purchase?(y/n): ").lower()
                if decision == "n":
                    restock_loop = False
                else:
                    display_products(products)
            except Exception as e:
                # Handle errors in restock process
                print(f"Error processing restock: {e}")
                print("Please try again\n")

        # Generate invoice and update database
        generate_purchase_invoice(vendor_name, restock_items, grand_total_cost)
        update_database(products, database_name)
        print("-" * 150)
        print("RESTOCK COMPLETE")
        print("-" * 150)
    except Exception as e:
        # Catch all other exceptions
        print(f"An error occurred during restocking process: {e}")
        print("Returning to main menu...\n")

def option_3():
    """Exits the system with a farewell message."""
    print("Thank you for using the system")
