import random
import time
from orders import Order

# MODIFY LOGIC AFTER MARKET BEHAVIOR IMPLEMENTATION

def order(
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
    symbol = random.choice(["AAPL", "MSFT", "NVDA", "GOOGL", "BRK.B", "BA", "TSLA", "NFLX"])

    return Order(side, price, qty, symbol, "indv")

for _ in range(100):
    o = order()
    print(o)
    time.sleep(0.05)