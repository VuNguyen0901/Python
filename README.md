# Local Produce Hub

A Python application that simulates a local produce marketplace with carbon footprint tracking and eco-friendly discount strategies.

## Features

- **Product Management** – Track produce with name, price, weight, and transport distance
- **Local vs Imported Produce** – Distinguish between local and imported products with different carbon footprint calculations
- **Carbon Footprint Tracking** – Calculate CO2 emissions based on transport distance, weight, and method (Air/Sea)
- **Shopping Cart** – Add products and checkout with automatic price calculation
- **Discount Strategies** – Pluggable discount system using the Strategy pattern
  - `EcoFriendlyDiscount` – 10% off when all cart items are local produce
  - `StandardDiscount` – No discount (default)

## Class Hierarchy

| Class | Description |
|---|---|
| `Product` | Base class for all produce items |
| `LocalProduce(Product)` | Locally sourced produce with lower carbon footprint |
| `ImportProduce(Product)` | Imported produce with transport method tracking |
| `Cart` | Shopping cart with configurable discount strategy |
| `DiscountStrategy` | Abstract base class for discount strategies |
| `EcoFriendlyDiscount` | Rewards all-local carts with 10% discount |
| `StandardDiscount` | No discount applied |

## Usage

```python
from local_produce_hub_class import *

# Create a cart with eco-friendly discount
cart = Cart(discount_strategy=EcoFriendlyDiscount())

# Add local produce
tomato = LocalProduce(name="Tomato", price=1.0, weight=1, transport_distance=3)
cart.add_product(tomato)

# Add imported produce
apple = ImportProduce(name="Apple", price=20, weight=1, transport_distance=1000, transport_method="Air")
cart.add_product(apple)

# Checkout
cart.display_cart()
cart.checkout()
```

## Running Tests

```bash
python local_produce_hub_test.py
```
