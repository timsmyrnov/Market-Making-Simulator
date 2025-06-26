import random
import time
from quotes import Quote

class MarketMaker:
    def __init__(
        self,
        mm_type: str = "PMM", # "PMM", "CMM", or "Preferred"
        max_spread: float = 0.50,
        quote_lifetime: float = 5.0,
        aggressiveness: float = 0.7, # 0.0 - 1.0
        max_inventory_size: int = 1000,
        circuit_breaker_enabled: bool = True
    ) -> None:
        self.type = mm_type
        self.max_spread = max_spread
        self.quote_lifetime = quote_lifetime
        self.aggressiveness = aggressiveness
        self.max_inventory_size = max_inventory_size
        self.circuit_breaker = circuit_breaker_enabled

    def quote(
        mid_price: float = 100.00,
        base_spread: float = 0.1,
        spread_volatility: float = 0.02,
        min_size: int = 100,
        max_size: int = 1000
    ) -> Quote:

        spread = base_spread + random.uniform(-spread_volatility, spread_volatility)
        spread = round(max(0.01, spread), 2)

        half_spread = spread / 2
        bid = round(mid_price - half_spread, 2)
        ask = round(mid_price + half_spread, 2)

        bid_size = random.randint(min_size, max_size)
        ask_size = random.randint(min_size, max_size)

        return Quote(bid=bid, ask=ask, bid_size=bid_size, ask_size=ask_size)

    for i in range(100):
        q = quote()
        print(q)
        time.sleep(0.05)