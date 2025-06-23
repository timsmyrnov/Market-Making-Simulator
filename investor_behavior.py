import random
import time
from orders import Order

# MODIFY LOGIC AFTER MARKET BEHAVIOR IMPLEMENTATION

def generate_order(
    mid_price: float = 100.00,
    price_volatility: float = 0.50,
    min_qty: int = 100,
    max_qty: int = 1000
) -> Order:
    """
    Generates a random order (buy or sell) around a mid-price
    """
    side = random.choice(["BUY", "SELL"])

    price_fluctuation = random.uniform(-price_volatility, price_volatility)
    price = round(mid_price + price_fluctuation, 2)

    qty = random.randint(min_qty, max_qty)

    return Order(side=side, price=price, qty=qty)

for _ in range(100):
    o = generate_order()
    print(o)
    time.sleep(0.05)