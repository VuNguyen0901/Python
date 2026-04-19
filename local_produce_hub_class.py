from abc import ABC, abstractmethod
class Product:
    def __init__(self, name, price, weight, transport_distance=0):
        self.name = name
        self.price = price
        self.weight = weight
        self.distance_km = transport_distance
        self.__import_price = price * 0.8  # Private attribute for import price

    def display_info(self):
        print(f"Product Name: {self.name}")
        print(f"Price: ${self.price:.2f}")
        print(f"Distance: {self.distance_km} km")

    @property
    def import_price(self):
        return self.__import_price
    
    def calculate_carbon_footprint(self):
        # Simple carbon footprint calculation based on distance
        return self.distance_km * 0.5  # Example: 0.5 kg CO2 per km

class Cart: 
    def __init__(self, discount_strategy=None):
        self.products = []
        self.discount_strategy = discount_strategy

    def add_product(self, product):
        self.products.append(product)

    def checkout(self):
        total_price = sum(product.price for product in self.products)
        discount = self.discount_strategy.apply_discount(self.products)
        final_price = total_price - discount
        print(f"Total Price: ${total_price:.2f}")
        print(f"Discount: ${discount:.2f}")
        print(f"Final Price: ${final_price:.2f}")
        print("-" * 30)

    def display_cart(self):
        print("Cart Contents:")
        for product in self.products:
            product.display_info()
            print("-" * 20)
class LocalProduce(Product):
    def __init__(self, name, price, weight, transport_distance=0):
        super().__init__(name, price, weight, transport_distance)
        self.farm_name = "Local Farm"

    def display_info(self):
        super().display_info()
        print(f"Local Produce: Yes (Distance: {self.distance_km} km)")

    def calculate_carbon_footprint(self):
        # Local produce has a lower carbon footprint
        co2_factor = 0.05
        return self.weight * self.distance_km * co2_factor  # Example: 0.05 kg CO2 per km

class ImportProduce(Product):
    def __init__(self, name, price, weight, transport_distance=0, transport_method="Air"):
        super().__init__(name, price, weight, transport_distance)
        self.country_of_origin = "Imported"
        self.transport_method = transport_method

    def display_info(self):
        super().display_info()
        print("Local Produce: No (Imported)")
        print(f"Transport Method: {self.transport_method}")

    def calculate_carbon_footprint(self):
        # Import produce has a higher carbon footprint based on transport method
        if self.transport_method == "Air":
            co2_factor = 0.5  # Example: 0.5 kg CO2 per km for air transport
        elif self.transport_method == "Sea":
            co2_factor = 0.1  # Example: 0.1 kg CO2 per km for sea transport
        else:
            co2_factor = 0.05  # Default for other transport methods
        return self.weight * self.distance_km * co2_factor
    
class DiscountStrategy(ABC):
    @abstractmethod
    def apply_discount(self, total_price):
        pass

class EcoFriendlyDiscount(DiscountStrategy):
    def apply_discount(self, items):
        total_price = sum(item.price for item in items)

        # Check if all items are local produce, will discount 10% if all items are local produce
        is_local_produce = all(isinstance(item, LocalProduce) for item in items)

        if is_local_produce:
            return total_price * 0.1  # 10% discount for eco-friendly products

        return 0

class StandardDiscount(DiscountStrategy):
    def apply_discount(self, total_price):
        return 0