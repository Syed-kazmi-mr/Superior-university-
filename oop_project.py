
from abc import ABC, abstractmethod

class Categories(ABC):
    """
    Abstract base class for clothing categories (Tops, Bottoms, Cordsets).
    This will define common methods that must be implemented by subclasses.
    """
    def __init__(self, category_name):
        self.category_name = category_name

    @abstractmethod
    def show_details(self):
        pass

    @abstractmethod
    def show_sizes(self):
        pass

    @abstractmethod
    def show_colors(self):
        pass

    @abstractmethod
    def select_size_and_color(self):
        pass

    def show_category(self):
        """
        Method to show the category name.
        """
        return f"Category: {self.category_name}"


# Subclass for Tops
class Tops(Categories):
    """
    Subclass for Tops category that inherits from Categories.
    Implements abstract methods.
    """
    def __init__(self, category_name, details, sizes, colors, price):
        super().__init__(category_name)
        self.details = details
        self.sizes = sizes
        self.colors = colors
        self.price = price

    def show_details(self):
        return f"Tops Details: {self.details}"

    def show_sizes(self):
        return f"Available Sizes: {', '.join(self.sizes)}"

    def show_colors(self):
        return f"Available Colors: {', '.join(self.colors)}"

    def select_size_and_color(self):
        while True:
            print(self.show_sizes())
            size = input("Choose a size: ").lower()
            if size not in self.sizes:
                print("Invalid size selected. Please choose a valid size.")
                continue

            print(self.show_colors())
            color = input("Choose a color: ").lower()
            if color not in self.colors:
                print("Invalid color selected. Please choose a valid color.")
                continue

            return f"You have selected Size: {size} and Color: {color}"


# Subclass for Bottoms
class Bottoms(Categories):
    """
    Subclass for Bottoms category that inherits from Categories.
    Implements abstract methods.
    """
    def __init__(self, category_name, details, sizes, colors, price):
        super().__init__(category_name)
        self.details = details
        self.sizes = sizes
        self.colors = colors
        self.price = price

    def show_details(self):
        return f"Bottoms Details: {self.details}"

    def show_sizes(self):
        return f"Available Sizes: {', '.join(self.sizes)}"

    def show_colors(self):
        return f"Available Colors: {', '.join(self.colors)}"

    def select_size_and_color(self):
        while True:
            print(self.show_sizes())
            size = input("Choose a size: ").lower()
            if size not in self.sizes:
                print("Invalid size selected. Please choose a valid size.")
                continue

            print(self.show_colors())
            color = input("Choose a color: ").lower()
            if color not in self.colors:
                print("Invalid color selected. Please choose a valid color.")
                continue

            return f"You have selected Size: {size} and Color: {color}"


# Subclass for Cordsets
class Cordsets(Categories):
    """
    Subclass for Cordsets category that inherits from Categories.
    Implements abstract methods.
    """
    def __init__(self, category_name, details, sizes, colors, price):
        super().__init__(category_name)
        self.details = details
        self.sizes = sizes
        self.colors = colors
        self.price = price

    def show_details(self):
        return f"Cordsets Details: {self.details}"

    def show_sizes(self):
        return f"Available Sizes: {', '.join(self.sizes)}"

    def show_colors(self):
        return f"Available Colors: {', '.join(self.colors)}"

    def select_size_and_color(self):
        while True:
            print(self.show_sizes())
            size = input("Choose a size: ").lower()
            if size not in self.sizes:
                print("Invalid size selected. Please choose a valid size.")
                continue

            print(self.show_colors())
            color = input("Choose a color: ").lower()
            if color not in self.colors:
                print("Invalid color selected. Please choose a valid color.")
                continue

            return f"You have selected Size: {size} and Color: {color}"


class Billing:
    """
    Billing system to calculate the total and handle payments.
    """
    @staticmethod
    def show_bill(selected_item):
        print(f"\n--- Billing Summary ---")
        print(f"Category: {selected_item.category_name}")
        print(f"Details: {selected_item.show_details()}")
        print(f"Price: ${selected_item.price}")
        print("-----------------------")
        return selected_item.price

    @staticmethod
    def process_payment(price):
        """
        Process the payment and ask for user details.
        """
        print("\n--- Payment ---")
        name = input("Enter your full name: ").strip()
        phone_number = input("Enter your phone number: ").strip()

        print(f"Processing payment of ${price}...")
        payment_method = input("Enter payment method (credit/debit): ").strip().lower()

        if payment_method in ['credit', 'debit']:
            print(f"Payment successful! Thank you for your purchase, {name}.")
            print(f"Your order will be delivered in 3-5 business days.")
        else:
            print("Payment failed. Please try again.")

        return name, phone_number


class Exit:
    """
    Exit class to terminate the program.
    """
    @staticmethod
    def exit_program():
        print("Exiting the program.")
        exit()  # Stops the program immediately


# Main function to interact with the user

# Creating objects of the subclasses with sizes, colors, and prices
tops = Tops("Tops", "Cotton, comfortable, casual wear", ["s", "m", "l", "xl"], ["red", "blue", "green"], 20)
bottoms = Bottoms("Bottoms", "Denim, slim fit, stylish", ["s", "m", "l"], ["black", "gray", "beige"], 25)
cordsets = Cordsets("Cordsets", "Premium quality, warm, perfect for winter", ["m", "l", "xl"], ["navy", "black", "white"], 30)

while True:
    # Ask user whether to continue to categories or exit
    print("Welcome to the Clothing Store!")
    print("Would you like to:")
    print("1. Browse Categories")
    print("2. Exit")
    choice = input("Enter 1 to browse categories or 2 to exit: ").strip()

    if choice == "1":
        # Let the user choose a category
        print("Please choose a category:")
        print("1. Tops ($20)")
        print("2. Bottoms ($25)")
        print("3. Cordsets ($30)")
        category_choice = input("Enter the number corresponding to your choice: ").strip()

        if category_choice == "1":
            selected_category = tops
        elif category_choice == "2":
            selected_category = bottoms
        elif category_choice == "3":
            selected_category = cordsets
        else:
            print("Invalid choice! Exiting...")
            Exit.exit_program()

        # Show category details
        print(selected_category.show_category())
        print(selected_category.show_details())
        print(selected_category.show_sizes())
        print(selected_category.show_colors())

        # Select size and color with validation
        selection = selected_category.select_size_and_color()
        print(selection)

        # Confirm order before billing
        confirm = input(f"Do you want to confirm the order? (yes/no): ").strip().lower()
        if confirm == "yes":
            # Billing system
            total_price = Billing.show_bill(selected_category)

            # Process payment
            Billing.process_payment(total_price)
        else:
            print("Order cancelled. Returning to the main menu.")
            continue  # Restart the program after cancelling the order

    elif choice == "2":
        # Exit the program immediately
        Exit.exit_program()

    else:
        print("Invalid choice! Exiting...")
        Exit.exit_program()