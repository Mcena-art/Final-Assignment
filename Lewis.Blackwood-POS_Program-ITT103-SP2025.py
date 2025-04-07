# Product catalog
product_catalog = {
    "Apple": {"price": 100.00, "stock": 10},
    "Ripe Banana": {"price": 150.00, "stock": 20},
    "Palmolive Bath Soap": {"price": 150.00, "stock": 15},
    "Serge Milk": {"price": 700.00, "stock": 5},
    "National White Bread": {"price": 500.00, "stock": 8},
    "Wata Water": {"price": 300.00, "stock": 12},
    "CB Chicken": {"price": 2000, "stock": 7},
    "Jasmine Rice": {"price": 270.00, "stock": 10},
    "1 L Pepsi": {"price": 300.00, "stock": 6},
    "Colgate Toothpaste": {"price": 450.00, "stock": 4},
}

# Shopping cart : Stores selected products and their quantities
shopping_cart = {}

#Function to display available products and their details
def display_products():
    print("\nAvailable Products:")
    for product, details in product_catalog.items():
        print(f"{product}: ${details['price']} (Stock: {details['stock']})")

#Function to add a product to the shopping cart
def add_to_cart(product_name, quantity):
    if product_name in product_catalog:
        if product_catalog[product_name]["stock"] >= quantity:
            shopping_cart[product_name] = shopping_cart.get(product_name, 0) + quantity
            product_catalog[product_name]["stock"] -= quantity
            print(f"Added {quantity} x {product_name} to the cart.")
        else:
            print(f"Insufficient stock for {product_name}. Available Quantity: {product_catalog[product_name]['stock']}")
    else:
        print("Product not found. Please enter a vaild product name")

#Function to remove a product from the shopping cart
def remove_from_cart(product_name, quantity):
    if product_name in shopping_cart:
        if shopping_cart[product_name] >= quantity:
            shopping_cart[product_name] -= quantity
            product_catalog[product_name]["stock"] += quantity
            if shopping_cart[product_name] == 0:
                del shopping_cart[product_name]
            print(f"Removed {quantity} x {product_name} from the cart.")
        else:
            print(f"Cannot remove {quantity} x {product_name}. Only {shopping_cart[product_name]} in cart.")
    else:
        print("Product not in cart. Please enter an item in your cart. ")
 
#Function to view items in the shopping cart
def view_cart():
    print("\nShopping Cart:")
    total_price = 0
    for product, quantity in shopping_cart.items():
        item_total = product_catalog[product]["price"] * quantity
        total_price += item_total
        print(f"{product}: {quantity} x ${product_catalog[product]['price']} = ${item_total:.2f}")
    print(f"Subtotal: ${total_price:.2f}")
    return total_price

#Function to process checkout, apply discounts, and calculate total amount
def checkout():
    subtotal = view_cart()
    discount = 0

# Apply a 5% discount if subtotal exceeds 5000
    if subtotal > 5000:
        discount = subtotal * 0.05
        subtotal -= discount
# cCalculates a 10% sales tax
    tax = subtotal * 0.10
    total_due = subtotal + tax

    while True:
        try:
            amount_received = float(input("Enter amount received from customer: $"))
            if amount_received < total_due:
                print("Amount received is less than total due. Please enter a valid amount.")
            else:
                change = amount_received - total_due
                generate_receipt(subtotal, tax, total_due, amount_received, change, discount)
                break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

#Function to generate and print a receipt
def generate_receipt(subtotal, tax, total_due, amount_received, change, discount):
    print("\n--- Receipt ---")
    print("Best Buy Retail Store ")
    print("TEL (876) 492-2834")
    print("23A Swallawfield Road, Kingston 5 ")
    print("Cashier Name: McEna Blackwood")
    print("Items Purchased:")
    
    for product, quantity in shopping_cart.items():
        item_total = product_catalog[product]["price"] * quantity
        print(f"{product}: {quantity} x ${product_catalog[product]['price']} = ${item_total:.2f}")

    print(f"\nSubtotal: ${subtotal + discount:.2f}")
    
    if discount > 0:
        print(f"Discount (5%): -${discount:.2f}")

    print(f"Sales Tax (10%): ${tax:.2f}")
    print(f"Total Amount Due: ${total_due:.2f}")
    print(f"Amount Paid: ${amount_received:.2f}")
    print(f"Change: ${change:.2f}")
    print("\nThank You for Shopping with us!")
    print("------------------------")

#Function to check for low-stock items
def low_stock_alert():
    print("\nLow Stock Alert:")
    for product, details in product_catalog.items():
        if details["stock"] < 5:
            print(f"{product} is low on stock (Available: {details['stock']})")

# Main function to handle the shopping process
def main():
    while True:
        display_products()
        print("\nOptions:")
        print("1. Add to Cart")
        print("2. Remove from Cart")
        print("3. View Cart")
        print("4. Checkout")
        print("5. Exit")

        option = input("Select an option (1-5): ")

        if option == "1":
            product_name = input("Enter product name: ")
            try:
                quantity = int(input("Enter quantity: "))
                add_to_cart(product_name, quantity)
            except ValueError:
                print("Invalid quantity. Please enter a number.")
        elif option == "2":
            product_name = input("Enter product name: ")
            try:
                quantity = int(input("Enter quantity to remove: "))
                remove_from_cart(product_name, quantity)
            except ValueError:
                print("Invalid quantity. Please enter a number.")
        elif option == "3":
            view_cart()
        elif option == "4":
            checkout()
            break
        elif option == "5":
            print("Thank you for visiting Best Buy Retail Store!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

#Run the main function when the script is executed
if __name__ == "__main__":
    main()
