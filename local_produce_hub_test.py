#%%
from local_produce_hub_class import *
def test_mixed_cart(cart):
    banana = LocalProduce(name="Banana", price=0.5, weight=1, transport_distance=2)
    durian = LocalProduce(name="Durian", price=3.0, weight=2, transport_distance=5)
    apple = ImportProduce(name="Apple", price=20, weight=1, transport_distance=1000, transport_method="Air")

    cart.add_product(banana)
    cart.add_product(durian)
    cart.add_product(apple)
    cart.display_cart()
    cart.checkout()

def test_local_produce_cart(cart):
    tomato = LocalProduce(name="Tomato", price=1.0, weight=1, transport_distance=3)
    cucumber = LocalProduce(name="Cucumber", price=0.8, weight=1, transport_distance=4)

    cart.add_product(tomato)
    cart.add_product(cucumber)
    cart.display_cart()
    cart.checkout()
#%%
if __name__ == "__main__":
    #%%
    cart = Cart(discount_strategy=EcoFriendlyDiscount())
    #%%
    test_mixed_cart(cart)
    #%%
    test_local_produce_cart(cart)
# %%

# %%
