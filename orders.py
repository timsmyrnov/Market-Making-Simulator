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

        self.id = generate_order_id()
        self.side = side.upper()
        self.price = price
        self.qty = qty

    def __str__(self) -> str:
        return (
            f"\033[96m#{self.id}\033[0m: "
            f"{'\033[92m' if self.side == 'BUY' else '\033[91m'}{self.side}\033[0m "
            f"\033[93m{self.qty}\033[0m @ \033[95m${self.price:.2f}\033[0m"
        )

order1 = Order("buy", 100.00, 20)
order2 = Order("SELL", 200.00, 60)

print(order1)
print(order2)