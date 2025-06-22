class Quote:
    def __init__(self, bid: float, ask: float) -> None:
        if bid >= ask:
            raise ValueError("Bid must be less than Ask.")
        self.bid = bid
        self.ask = ask

    def spread(self) -> float:
        return self.ask - self.bid

    def mid_price(self) -> float:
        return (self.bid + self.ask) / 2

    def update(self, bid: float, ask: float) -> None:
        if bid >= ask:
            raise ValueError("Bid must be less than Ask.")
        self.bid = bid
        self.ask = ask

    def __str__(self) -> str:
        return f"Bid: {self.bid:.2f}, Ask: {self.ask:.2f} (Spread: {self.spread():.2f})"