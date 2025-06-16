def load_data(database_name):
    """
    Loads product data from a given text file.

    Args:
        database_name (str): The name of the file containing product data.

    Returns:
        list: A list of product dictionaries loaded from the file.
    """
    try:
        with open(database_name, "r") as file:
            products = []
            product_id = 0  # Unique ID for each product
            
            for line in file:
                if not line.strip():
                    continue  # Skip blank lines

                try:
                    product_details = line.strip().split(",")
                    
                    # Ensure the line has all required fields
                    if len(product_details) < 5:
                        print(f"Error: Line '{line.strip()}' doesn't have enough fields. Skipping...")
                        continue
                    
                    # Create product dictionary
                    product = {
                        "id": product_id,
                        "name": product_details[0],
                        "brand": product_details[1],
                        "stock": int(product_details[2]),
                        "cost_price": float(product_details[3]),
                        "country": product_details[4].strip(),
                    }
                    product_id += 1
                    products.append(product)
                except (IndexError, ValueError) as e:
                    # Handle malformed lines or type conversion errors
                    print(f"Error processing line: {line.strip()}. Error: {e}. Skipping...")
                    continue
                    
            return products
    except FileNotFoundError:
        # Handle case where file does not exist
        print(f"Error: File '{database_name}' not found. Creating a new empty database.")
        return []
    except Exception as e:
        # Catch-all for any unexpected errors
        print(f"An unexpected error occurred while loading data: {e}")
        return []
