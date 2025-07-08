import random
import time
from orders import Order

def order(symbol: str, data: dict) -> Order:
    mid_price = data[symbol]
    volatility = 0.50
    min_qty = 100
    max_qty = 1000

    side = random.choice(["BUY", "SELL"])

    fluct = random.uniform(-volatility, volatility)
    price = round(mid_price + fluct, 2)

    qty = random.randint(min_qty, max_qty)

    return Order(side, price, qty, symbol, "indv")

if __name__ == "__main__":
    print(order("MSFT", {"AAPL": 101, "MSFT": 201}))