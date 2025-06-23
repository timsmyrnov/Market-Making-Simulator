import itertools

_order_id_generator = itertools.count(1)

def generate_order_id() -> int:
    return next(_order_id_generator)

class Order:
    def __init__(self, side: str, price: float, qty: int) -> None:
        if qty <= 0:
            raise ValueError("Quantity must be greater than 0.")

        if side.upper() not in {"BUY", "SELL"}:
            raise ValueError("Side must be 'BUY' or 'SELL'.")

        self.side = side.upper()
        self.price = price
        self.qty = qty

        self.id = generate_order_id()

    def __str__(self) -> str:
        return (
            f"\033[96m#{self.id}\033[0m: "
            f"{'\033[92m' if self.side == 'BUY' else '\033[91m'}{self.side}\033[0m "
            f"\033[93m{self.qty}\033[0m @ \033[95m${self.price:.2f}\033[0m"
        )
    
if __name__ == "__main__":
    orders = [
        Order("BUY", 99.50, 500),
        Order("SELL", 99.55, 300),
        Order("BUY", 100.00, 1000),
        Order("SELL", 100.05, 800),
        Order("BUY", 100.20, 200),
        Order("SELL", 100.30, 150),
        Order("BUY", 99.75, 750),
        Order("SELL", 99.85, 500),
        Order("BUY", 101.10, 100),
        Order("SELL", 101.25, 50),
    ]

    for o in orders:
        print(o)