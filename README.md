# Point-of-Sale-System-
This Point of Sale system represents a simple console-based shopping cart system for a retail store. It allows users to view products, add items to their shopping cart, remove items, view their cart, and proceed to checkout.

Gabrielle Lewis and McEna Blackwood
April 01, 2025
Course: ITT103

# How to run the system 

The product_catalog is a dictionary where:
+  Keys → Product names (e.g., "Apple", "1 L Pepsi")
+  Values → Another dictionary containing:
+ "price" → The cost of the product.
+  "stock" → The available quantity.
We are going to use apples for example. 

This means:
+  An Apple costs $100.00.
+  There are 10 Apples in stock.
The shopping_cart dictionary keeps track of:
+  Products the user has selected.
+  The quantity of each product.
The function display_product prints all available products, their prices, and remaining stock.

How It Works
+  It loops through the product_catalog and displays each item.
+  Uses an f-string to format the output.
The add to cart function allows the user to add products to their shopping cart.

How It Works
1.  Checks if the product exists in product_catalog:
+  ✅ Valid Product → Proceeds to check stock.
+ ❌ Invalid Product → Prints "Product not found."
2.  Checks if enough stock is available:
+ ✅ Sufficient Stock → Adds item to cart and reduces stock.
+  ❌ Insufficient Stock → Displays available stock and doesn't add.

Valid user Input
Lets say we want to add 3 apples to our shopping cart. 
+  "Apple" exists in product_catalog.
+  The current stock (10) is greater than or equal to 3.
+ shopping_cart is updated with 3 apples
  
What will also happen is that the stock for apples will also reduce. 
The output of this function would be 3 apples added to the shopping cart. 

Let’s use an invalid output. 

Let’s say we enter orange into our system. Orange is not in our product catalog. Because orange is not in our product catalog the system will output product not found. Please enter a valid product name. 
Our next invalid input would be insufficient stock. 
Let’s say a customer wants 8 toothpaste but there is only 4 in stock. The user will get an output saying insufficient stock for Colgate Toothpaste. Available Quantity: 4

Removing Products from the Cart:
Check if the item is in the cart: The system first looks to see if the product the user wants to remove is actually in their shopping cart.
Ensure valid removal: It makes sure the user isn't trying to take out more of the product than they originally added to the cart.

If everything is okay:
It reduces the quantity of that product in the cart.
It increases the available stock of that product back in the main product list (catalog).
If the quantity in the cart reaches zero: The product is completely removed from the shopping cart.

2. Viewing the Cart:Loop through the cart: The system goes through each item in the shopping cart.
Calculate total cost: It figures out how much each product costs in total.
Display subtotal: It shows the total amount before any taxes or discounts are applied.

3. Checkout Process:
Show the cart total: It calls a function to display the total cost of everything in the cart.
Apply discounts: If the subtotal is over $5000, a 5% discount is applied.
Calculate sales tax: A 10% sales tax is added to the total.
Payment input: The user is asked to enter how much money they are paying.
Check payment sufficiency:
If the payment is enough, it calculates how much change the user should get back and creates a receipt.
If the payment is not enough, it prompts the user to provide more money.

4. Generating the Receipt:
Display receipt: It shows a nicely formatted receipt.List items: The receipt includes each item purchased, its price, and how many were bought.
Show totals: It includes the subtotal, any discounts, tax, the total amount due, how much was paid, and the change given back.
5. Low Stock Alert:
Check stock levels: The system looks to see if any product has fewer than 5 items left in stock.
Print warning: If it finds any low-stock items, it prints a warning message to alert the user.

6. Main Menu:
Run continuously: The system keeps running in a loop, allowing the user to keep interacting with it.
Provide options: It shows a menu with different choices for the user to select from.

In summary, this code manages a shopping cart system by allowing users to add, remove, and view products, handle checkout and payments, alert for low stock, and provide a user-friendly interface through a main menu.

# What are the assumptions and limitations regarding the code operation ? 

## Assumptions:  

Single User Operation: Designed for one user or session at a time, with no support for multiple users or persistent sessions.

In memory storage: All data, including the cart and catalog, is stored in memory. When the program exits, all data will be lost.

Stock Is Updated Immediately: Stock is updated immediately when a product is added to the cart, reducing the stock as if a purchase will be completed.

Product Names Are Unique: Each product name is used as a unique identifier—there’s no handling for duplicate names.

## Limitations: 

No Case-I sensitive Matching: Typing “apple” instead of “Apple” won’t work—it’s case-sensitive.

No Currency Formatting or Localization: All amounts are treated as raw floats and displayed as is, without any locale-specific formatting, such as commas or currency symbols.

Hardcoded Store Info & Cashier Name: The store name, phone number, address, and cashier name are fixed and cannot be changed through input or configuration.

No Item Search or Filtering: Users must scroll through the entire product list manually—there’s no search, sorting, or filtering.

No Error Recovery on Checkout: If a customer changes their mind at checkout, there is no way to reverse the deduction from stock or return to the previous stage.
