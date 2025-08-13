from collections import deque
from typing import Deque, Dict
from orders import Order
from quotes import Quote

class OrderBook:
    def __init__(self) -> None:
        self.bids: Dict[float, Deque[Order]] = {}
        self.asks: Dict[float, Deque[Order]] = {}

    def handle_order(self, order: Order):
        if order.side == 'BUY':
            # Match bid to existing ask
            if order.order_type == 'LIMIT' and order.price in self.asks:
                total_ask_qty = sum(o.qty for o in self.asks[order.price])
                if order.qty < total_ask_qty:
                    return

            if order.price not in self.bids:
                self.bids[order.price] = deque()
            self.bids[order.price].append(order)

        else:
            # Match ask to existing bid
            if order.price in self.bids:
                total_bid_qty = sum(o.qty for o in self.bids[order.price])
                if order.qty < total_bid_qty:
                    return

            if order.price not in self.asks:
                self.asks[order.price] = deque()
            self.asks[order.price].append(order)

    def handle_quote(self, quote: Quote):
        bid_order = Order('BUY', quote.symbol, 'LIMIT', price=quote.bid, qty=quote.bid_size, src=quote.src)
        ask_order = Order('SELL', quote.symbol, 'LIMIT', price=quote.ask, qty=quote.ask_size, src=quote.src)

        self.handle_order(bid_order)
        self.handle_order(ask_order)

    def get_tob(self) -> tuple:
        bid = max(self.bids.keys(), default=None)
        ask = min(self.asks.keys(), default=None)

        bid_size = sum(o.qty for o in self.bids.get(bid, [])) if bid is not None else 0
        ask_size = sum(o.qty for o in self.asks.get(ask, [])) if ask is not None else 0

        spread = (ask - bid) if (bid is not None and ask is not None) else None
        return (bid, bid_size, ask, ask_size, spread)

    def __str__(self):
        output = []
        output.append('\n----- ORDER BOOK -----')

        output.append('\nBids:')
        for price in sorted(self.bids, reverse=True):
            total_qty = sum(order.qty for order in self.bids[price])
            output.append(f'  {price:.2f} x {total_qty}')

        output.append('\nAsks:')
        for price in sorted(self.asks):
            total_qty = sum(order.qty for order in self.asks[price])
            output.append(f'  {price:.2f} x {total_qty}')

        return '\n'.join(output)

if __name__ == '__main__':
    book = OrderBook()

    orders = [
        Order('BUY',  'AAPL', 'LIMIT', price=100.70, qty=60,  src='indv'),
        Order('SELL', 'AAPL', 'LIMIT', price=100.90, qty=100, src='hft'),
        Order('BUY',  'AAPL', 'LIMIT', price=100.65, qty=150, src='mm'),
        Order('SELL', 'AAPL', 'LIMIT', price=100.95, qty=80,  src='indv'),
        Order('BUY',  'AAPL', 'LIMIT', price=100.60, qty=120, src='mm'),
        Order('SELL', 'AAPL', 'LIMIT', price=101.00, qty=90,  src='hft'),
        Order('BUY',  'AAPL', 'LIMIT', price=100.55, qty=200, src='indv'),
        Order('SELL', 'AAPL', 'LIMIT', price=101.05, qty=50,  src='mm'),
        Order('BUY',  'AAPL', 'LIMIT', price=100.75, qty=70,  src='hft'),
        Order('SELL', 'AAPL', 'LIMIT', price=100.85, qty=130, src='indv'),
    ]

    quotes = [
        Quote(100.60, 100.85, 500, 300, 'AAPL'),
        Quote(100.62, 100.88, 1000, 800, 'AAPL'),
        Quote(100.70, 100.90, 200, 150, 'AAPL'),
        Quote(100.58, 100.86, 750, 500, 'AAPL'),
        Quote(100.76, 100.95, 100, 50, 'AAPL'),
        Quote(100.55, 100.89, 600, 700, 'AAPL'),
        Quote(100.73, 100.92, 350, 350, 'AAPL'),
        Quote(100.78, 100.96, 150, 120, 'AAPL'),
        Quote(100.80, 101.00, 90, 200, 'AAPL'),
        Quote(100.59, 100.87, 1000, 1000, 'AAPL'),
    ]

    for o, q in zip(orders, quotes):
        book.handle_order(o)
        book.handle_quote(q)

    print(book)
    print(book.get_tob())