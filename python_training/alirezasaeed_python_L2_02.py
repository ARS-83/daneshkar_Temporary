from print_color import print
from typing import List, Optional
import os


class Product:
    """
    Represents a product in the store.
    """

    def __init__(self, name: str, price: float, stock: int) -> None:
        self.name: str = name
        self.price: float = price
        self.stock: int = stock

    def __str__(self) -> str:
        return f"{self.name} - ${self.price:.2f} (Stock: {self.stock})"


class Store:
    """
    Manages store products.
    """

    def __init__(self) -> None:
        self.products: List[Product] = []

    def add_product(self, name: str, price: float, stock: int) -> None:
        self.products.append(Product(name, price, stock))

    def list_products(self) -> None:
        if not self.products:
            print("No products available.", color="yellow")
            return

        for index, product in enumerate(self.products, start=1):
            print(f"[{index}] {product}")

    def find_product(self, name: str) -> Optional[Product]:
        for product in self.products:
            if product.name.lower() == name.lower():
                return product
        return None


class CartItem:
    """
    Represents an item inside the shopping cart.
    """

    def __init__(self, product: Product, quantity: int) -> None:
        self.product: Product = product
        self.quantity: int = quantity

    def total_price(self) -> float:
        return self.product.price * self.quantity


class Cart:
    """
    Shopping cart management.
    """

    def __init__(self) -> None:
        self.items: List[CartItem] = []

    def add_to_cart(self, product: Product, quantity: int) -> bool:
        if quantity > product.stock:
            print("Not enough stock available.", color="yellow")
            return False

        for item in self.items:
            if item.product == product:
                item.quantity += quantity
                product.stock -= quantity
                return True

        self.items.append(CartItem(product, quantity))
        product.stock -= quantity
        return True

    def remove_from_cart(self, product_name: str) -> None:
        for item in self.items:
            if item.product.name.lower() == product_name.lower():
                item.product.stock += item.quantity
                self.items.remove(item)
                print(f"Removed {product_name} from cart.", color="magenta")
                return

        print("Item not found in cart.", color="yan")

    def view_cart(self) -> None:
        if not self.items:
            print("Your cart is empty.", color="yellow")
            return

        print("Your cart:")
        for item in self.items:
            print(f"- {item.product.name} x{item.quantity} - ${item.total_price():.2f}", color="yan")

        print(f"Total: ${self.total_price():.2f}", color="purple")


    def total_price(self) -> float:
        return sum(item.total_price() for item in self.items)


def manager_login() -> bool:
    print("Store Manager Login", color="purple")
    username = input("Username: ")
    password = input("Password: ")

    return username == "admin" and password == "1234"


def manager_panel(store: Store) -> None:
    print("Add Products", color="green")
    while True:
        name = input("Enter product name (or 'done' to finish): ")
        if name.lower() == "done":
            break

        price = float(input("Enter product price: "))
        stock = int(input("Enter product stock quantity: "))
        store.add_product(name, price, stock)

        print(f"Product added: {name} - ${price:.2f} (Stock: {stock})", color="green")


def customer_panel(store: Store) -> None:
    cart = Cart()

    while True:
        print("\nAvailable products:", color="blue")
        store.list_products()

        print("\n1. Add item to cart", color="green")
        print("2. Remove item from cart", color="green")
        print("3. View cart", color="green")
        print("4. Checkout", color="green")
        print("5. View Product List", color="green")
        print("6. Return to main menu", color="green")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter product name: ")
            product = store.find_product(name)
            if not product:
                os.system("cls" if os.name == "nt" else "clear")
                print("Product not found.", color="yellow")
                continue

            quantity = int(input("Enter quantity: "))
            if cart.add_to_cart(product, quantity):
                os.system("cls" if os.name == "nt" else "clear")
                print(f"Added {quantity} x {product.name} to cart.", color="blue")

        elif choice == "2":
            name = input("Enter product name to remove: ")
            cart.remove_from_cart(name)

        elif choice == "3":
            cart.view_cart()

        elif choice == "4":
            os.system("cls" if os.name == "nt" else "clear")
            print("Final Checkout:", color="purple")
            cart.view_cart()
            print("Thank you for shopping with us!", color="green")
            break

        elif choice == "5":
            if not store.products:
                os.system("cls" if os.name == "nt" else "clear")
                print("No Products Available", color="yellow")
                continue

            store.list_products()
            product_code = input("Enter Product Index")
            if not product_code.isdigit():
                os.system("cls" if os.name == "nt" else "clear")
                print(f"Please Enter Number!", color="red")
                continue

            product = store.products[(int(product_code) - 1)]
            print(" You Is Adding [%s] Product In Your Cart " % product.name, color="green")
            quantity = int(input("Enter quantity: "))
            if cart.add_to_cart(product, quantity):
                os.system("cls" if os.name == "nt" else "clear")
                print(f"Added {quantity} x {product.name} to cart.", color="green")

        elif choice == "6":
            break

        else:
            os.system("cls" if os.name == "nt" else "clear")
            print("Invalid choice.", color="red")


def main() -> None:
    store = Store()

    while True:
        print("\nMINI STORE MANAGEMENT SYSTEM", color="blue")
        print("1. Store Manager", color="purple")
        print("2. Customer", color="purple")
        print("3. Exit Program", color="purple")

        choice = input("Enter choice: ")

        if choice == "1":
            if manager_login():
                print("Login successful.", color="green")
                manager_panel(store)
            else:
                print("Login failed.", color="red")

        elif choice == "2":
            customer_panel(store)

        elif choice == "3":
            print("Goodbye!", color="green")
            break

        else:
            print("Invalid option.", color="red")


if __name__ == "__main__":
    print(""" Created By alirezasaeed 
   _____ 👑
  / ____| |
 | (___ | |_ ___  _ __ ___
  \\___ \\| __/ _ \\| '__/ _ \\
  ____) | || (_) | | |  __/
 |_____/ \\__\\___/|_|  \\___|
""", color="magenta")
    main()



























#  """


#        ,--.
#    ,--/  /|                                                              .--.--.       ___                                      
# ,---,': / '              ,--,                                           /  /    '.   ,--.'|_                                    
# :   : '/ /             ,--.'|                           __  ,-.        |  :  /`. /   |  | :,'   ,---.    __  ,-.                
# |   '   ,              |  |,      .--.--.             ,' ,'/ /|        ;  |  |--`    :  : ' :  '   ,'\ ,' ,'/ /|                
# '   |  /     ,--.--.   `--'_     /  /    '     ,---.  '  | |' |        |  :  ;_    .;__,'  /  /   /   |'  | |' | ,---.          
# |   ;  ;    /       \  ,' ,'|   |  :  /`./    /     \ |  |   ,'         \  \    `. |  |   |  .   ; ,. :|  |   ,'/     \         
# :   '   \  .--.  .-. | '  | |   |  :  ;_     /    /  |'  :  /            `----.   \:__,'| :  '   | |: :'  :  / /    /  |        
# |   |    '  \__\/: . . |  | :    \  \    `. .    ' / ||  | '             __ \  \  |  '  : |__'   | .; :|  | ' .    ' / |        
# '   : |.  \ ," .--.; | '  : |__   `----.   \'   ;   /|;  : |            /  /`--'  /  |  | '.'|   :    |;  : | '   ;   /|        
# |   | '_\.'/  /  ,.  | |  | '.'| /  /`--'  /'   |  / ||  , ;           '--'.     /   ;  :    ;\   \  / |  , ; '   |  / |        
# '   : |   ;  :   .'   \;  :    ;'--'.     / |   :    | ---'              `--'---'    |  ,   /  `----'   ---'  |   :    |        
# ;   |,'   |  ,     .-./|  ,   /   `--'---'   \   \  /                                 ---`-'                   \   \  /         
# '---'      `--`---'     ---`-'                `----'                                                            `----'          

# """