from collections import deque
from typing import Deque, Dict
from orders import Order
from quotes import Quote

class OrderBook:
    def __init__(self) -> None:
        self.bids: Dict[float, Deque[Order]] = {}
        self.asks: Dict[float, Deque[Order]] = {}

    def handle_order(self, order: Order):
        if order.side == "BUY":
            if order.price not in self.bids:
                self.bids[order.price] = deque()
            self.bids[order.price].append(order)

        else:
            if order.price not in self.asks:
                self.asks[order.price] = deque()
            self.asks[order.price].append(order)

    def handle_quote(self, quote: Quote):
        bid_order = Order("BUY", quote.bid, quote.bid_size, quote.symbol, quote.src)
        ask_order = Order("SELL", quote.ask, quote.ask_size, quote.symbol, quote.src)

        self.handle_order(bid_order)
        self.handle_order(ask_order)

    def __str__(self):
        output = []
        output.append("\n----- ORDER BOOK -----")

        output.append("\nBids:")
        for price in sorted(self.bids, reverse=True):
            total_qty = sum(order.qty for order in self.bids[price])
            output.append(f"  {price:.2f} x {total_qty}")

        output.append("\nAsks:")
        for price in sorted(self.asks):
            total_qty = sum(order.qty for order in self.asks[price])
            output.append(f"  {price:.2f} x {total_qty}")

        return "\n".join(output)

if __name__ == "__main__":
    book = OrderBook()
    o = Order("BUY", 101.0, 60, "AAPL", "indv")

    orders = [
        Order("BUY", 101.00, 60, "AAPL", "indv"),
        Order("SELL", 101.20, 100, "AAPL", "hft"),
        Order("BUY", 100.90, 150, "AAPL", "mm"),
        Order("SELL", 101.30, 80, "AAPL", "indv"),
        Order("BUY", 100.95, 120, "AAPL", "mm"),
        Order("SELL", 101.10, 90, "AAPL", "hft"),
        Order("BUY", 100.80, 200, "AAPL", "indv"),
        Order("SELL", 101.25, 50, "AAPL", "mm"),
        Order("BUY", 101.05, 70, "AAPL", "hft"),
        Order("SELL", 101.15, 130, "AAPL", "indv"),
    ]

    quotes = [
        Quote(99.50, 99.55, 500, 300, "AAPL"),
        Quote(100.00, 100.05, 1000, 800, "AAPL"),
        Quote(100.20, 100.30, 200, 150, "AAPL"),
        Quote(99.75, 99.85, 750, 500, "AAPL"),
        Quote(101.10, 101.25, 100, 50, "AAPL"),
        Quote(98.90, 99.10, 600, 700, "AAPL"),
        Quote(100.45, 100.50, 350, 350, "AAPL"),
        Quote(101.75, 101.80, 150, 120, "AAPL"),
        Quote(102.00, 102.15, 90, 200, "AAPL"),
        Quote(99.00, 99.20, 1000, 1000, "AAPL")
    ]

    for o, q in zip(orders, quotes):
        book.handle_order(o)
        book.handle_quote(q)

    print(book)