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
        bid_order = Order("BUY", quote.bid, quote.bid_size)
        ask_order = Order("SELL", quote.ask, quote.ask_size)

        self.handle_order(bid_order)
        self.handle_order(ask_order)