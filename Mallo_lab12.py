def display_menu():
    print("Menu:")
    print("1. spaghetti - ₱50.00")
    print("2. hotdog - ₱15.00")
    print("3. egg - ₱10.00")
    print("4. milo - ₱8.00")
    print("5.burger - ₱60.00")
                         
 

def main():
    # Display the menu
    display_menu()

    # Get the user's choice
    choice = int(input("Enter the number of the item you want to order: "))

    # Prices for the items
    if choice == 1:
        total_cost = 50.00
    elif choice == 2:
        total_cost = 15.00
    elif choice == 3:
        total_cost = 10.00
    elif choice == 4:
        total_cost = 8.00
    elif choice == 5:
        total_cost = 60.00
    else:
        print("Invalid choice!")
        return

    # Ask for the cash provided
    cash_given = float(input(f"The total cost is ₱{total_cost}. Please enter the cash amount: ₱"))

    # Check if the payment is sufficient
    while cash_given < total_cost:
        print(f"Insufficient amount! You still need ₱{total_cost - cash_given}. Please try again.")
        cash_given = float(input(f"Enter the cash amount: ₱"))

    # Calculate the change
    change = cash_given - total_cost
    print(f"Payment accepted. Your change is: ₱{change:.2f}")

    print("Thank you for your order!")

if __name__ == "__main__":
    main()