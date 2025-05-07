from abc import ABC, abstractmethod

class Product:
    def __init__(self, name, price, stock):
        self.__name = name
        self.__price = price
        self.__stock = stock

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_stock(self):
        return self.__stock

    def reduce_stock(self, qty):
        if qty <= self.__stock:
            self.__stock -= qty
            return True
        else:
            return False

    def display_info(self, index):
        print(f"{index}. {self.__name} - ₱{self.__price} - Stock: {self.__stock}")


class User(ABC):
    def __init__(self, name, email):
        self.name = name
        self.email = email

    @abstractmethod
    def get_role(self):
        pass


class Vendor(User):
    def __init__(self, name, email, store_name):
        super().__init__(name, email)
        self.store_name = store_name
        self.products = []

    def get_role(self):
        return "Vendor"

    def add_product(self, product):
        self.products.append(product)

    def display_products(self):
        print(f"\n{self.store_name}'s Products:")
        for i, product in enumerate(self.products, 1):
            product.display_info(i)


class Buyer(User):
    def __init__(self, name, email):
        super().__init__(name, email)

    def get_role(self):
        return "Buyer"

    def place_order(self, product, quantity):
        if product.reduce_stock(quantity):
            print(f"✅ Order successful: {quantity} x {product.get_name()}")
        else:
            print("❌ Not enough stock!")

def main():

    vendor = Vendor("Aling Nena", "nena@example.com", "Nena's Gulay")
    buyer = Buyer("Juan Dela Cruz", "juan@example.com")

    while True:
        print("\n📦 Lokal Market")
        print("1. Vendor - Add Product")
        print("2. Buyer - View & Buy Products")
        print("3. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter product name: ")
            price = float(input("Enter price: "))
            stock = int(input("Enter stock: "))
            product = Product(name, price, stock)
            vendor.add_product(product)
            print("✅ Product added.")

        elif choice == "2":
            if not vendor.products:
                print("❌ No products available.")
                continue

            vendor.display_products()
            try:
                selected = int(input("Select product number: ")) - 1
                quantity = int(input("Enter quantity: "))
                if 0 <= selected < len(vendor.products):
                    buyer.place_order(vendor.products[selected], quantity)
                else:
                    print("❌ Invalid selection.")
            except ValueError:
                print("❌ Invalid input.")

        elif choice == "3":
            print("👋 Exiting Lokal Market. Thank you!")
            break

        else:
            print("❌ Invalid choice.")

# Run the app
if __name__ == "__main__":
    main()
