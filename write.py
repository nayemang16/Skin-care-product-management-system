import datetime

def update_database(products, database_name):
    """
    Updates the product database file with current product information.

    Args:
        products (list): The current product list.
        database_name (str): The name of the product database file.
    """
    try:
        # Open file and write updated product information
        with open(database_name, "w") as file:
            for product in products:
                # Format each product as CSV line
                file.write(
                    product["name"]
                    + ","
                    + product["brand"]
                    + ","
                    + str(product["stock"])
                    + ","
                    + str(product["cost_price"])
                    + ","
                    + product["country"]
                )
                file.write("\n")
    except IOError as e:
        # Handle file writing errors
        print(f"Error updating database: {e}")
    except Exception as e:
        # Catch all other exceptions
        print(f"An unexpected error occurred while updating database: {e}")

def generate_invoice(customer_name, phone_number, item_selling, grand_total):
    """
    Generates and saves a customer invoice.

    Args:
        customer_name (str): The name of the customer.
        phone_number (str): The phone number of the customer.
        item_selling (list): List of items sold.
        grand_total (float): The total amount.
    """
    try:
        # Get current date and time for invoice
        date = datetime.datetime.now()
        today_date = date.strftime("%d-%m-%Y")
        time_now = date.strftime("%H:%M")
        
        # Create unique filename for invoice
        filename = f"invoice-{today_date}-{time_now.replace(':', '-')}-{customer_name}"
        
        # Define format strings for table alignment
        header_format = "{:<5} {:<25} {:<25} {:<15} {:<15} {:<15}"
        item_format = "{:<5} {:<25} {:<25} {:<15} {:<15.2f} {:<15.2f}"
        
        try:
            # Write invoice to file
            with open(filename, "w") as file:
                # Write invoice header
                file.write("INVOICE\n")
                file.write("-" * 100 + "\n")
                file.write(f"Customer Name: {customer_name}\n")
                file.write(f"Phone Number: {phone_number}\n")
                file.write(f"Date: {time_now}, {today_date}\n")
                file.write("-" * 100 + "\n")
                
                # Write table header
                file.write(header_format.format("S.N", "Name", "Brand Name", "Total quantity", "Rate", "Total per item"))
                file.write("\n" + "-" * 100 + "\n")
                
                # Write each item with formatting
                for i, item in enumerate(item_selling, 1):
                    file.write(item_format.format(
                        i,
                        item["name"],
                        item["brand"],
                        item["total_quantity"],
                        item["individual_item_price"],
                        item["total_item_price"]
                    ))
                    file.write("\n")
                    
                # Write total amount
                file.write("-" * 100 + "\n")
                file.write(f"Grand Total: {grand_total:.2f}\n")
        except IOError as e:
            # Handle file writing errors
            print(f"Error saving invoice to file: {e}")

        # Display invoice on screen
        print("\n" + "-" * 100)
        print("INVOICE")
        print("-" * 100)
        print(f"Customer Name: {customer_name}")
        print(f"Phone Number: {phone_number}")
        print(f"Date: {time_now}, {today_date}")
        print("-" * 100)
        
        print(header_format.format("S.N", "Name", "Brand Name", "Total quantity", "Rate", "Total per item"))
        print("-" * 100)
        
        for i, item in enumerate(item_selling, 1):
            print(item_format.format(
                i,
                item["name"],
                item["brand"],
                item["total_quantity"],
                item["individual_item_price"],
                item["total_item_price"]
            ))
        
        print("-" * 100)
        print(f"Grand Total: {grand_total:.2f}")
        print("-" * 100)
        print("\nPROCESS COMPLETE")
        print("-" * 100)
        print("\n")
    except Exception as e:
        # Catch all other exceptions
        print(f"Error generating invoice: {e}")

def generate_purchase_invoice(vendor_name, restock_items, grand_total_cost):
    """
    Generates and saves a vendor purchase invoice.

    Args:
        vendor_name (str): The name of the vendor.
        restock_items (list): List of items purchased.
        grand_total_cost (float): The total cost amount.
    """
    try:
        # Get current date and time for invoice
        date = datetime.datetime.now()
        today_date = date.strftime("%d-%m-%Y")
        time_now = date.strftime("%H:%M")
        
        # Create unique filename for invoice
        filename = f"invoice-{today_date}-{time_now.replace(':', '-')}-{vendor_name}"
        
        # Define format strings for table alignment
        header_format = "{:<5} {:<25} {:<25} {:<15} {:<15} {:<15}"
        item_format = "{:<5} {:<25} {:<25} {:<15} {:<15.2f} {:<15.2f}"
        
        try:
            # Write invoice to file
            with open(filename, "w") as file:
                # Write invoice header
                file.write("INVOICE\n")
                file.write("-" * 100 + "\n")
                file.write(f"Vendor Name: {vendor_name}\n")
                file.write(f"Date: {time_now}, {today_date}\n")
                file.write("-" * 100 + "\n")
                
                # Write table header
                file.write(header_format.format("S.N", "Name", "Brand Name", "Total quantity", "Rate", "Total per item"))
                file.write("\n" + "-" * 100 + "\n")
                
                # Write each item with formatting
                for i, item in enumerate(restock_items, 1):
                    file.write(item_format.format(
                        i,
                        item["name"],
                        item["brand"],
                        item["product_quantity"],
                        item["cost_price"],
                        item["total_item_cost"]
                    ))
                    file.write("\n")
                    
                # Write total amount
                file.write("-" * 100 + "\n")
                file.write(f"Grand Total: {grand_total_cost:.2f}\n")
        except IOError as e:
            # Handle file writing errors
            print(f"Error saving invoice to file: {e}")

        # Display invoice on screen
        print("-" * 100)
        print("INVOICE")
        print("-" * 100)
        print(f"Vendor Name: {vendor_name}")
        print(f"Date: {time_now}, {today_date}")
        print("-" * 100)
        
        print(header_format.format("S.N", "Name", "Brand Name", "Total quantity", "Rate", "Total per item"))
        print("-" * 100)
        
        for i, item in enumerate(restock_items, 1):
            print(item_format.format(
                i,
                item["name"],
                item["brand"],
                item["product_quantity"],
                item["cost_price"],
                item["total_item_cost"]
            ))
        
        print("-" * 100)
        print(f"Grand Total: {grand_total_cost:.2f}")
        print("-" * 100)
        print("\n")
    except Exception as e:
        # Catch all other exceptions
        print(f"Error generating purchase invoice: {e}")
