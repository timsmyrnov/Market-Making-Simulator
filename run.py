import time
import random
import yfinance as yf
import fetch_market_data as fmd
import order_book as ob
import market_behavior as mb
import investor_behavior as ib
import market_maker as mm

def run_simulation():
    AAPL_order_book = ob.OrderBook()
    market_maker = mm.MarketMaker()
    latest_data = fmd.download_latest_data(["AAPL", "MSFT", "GOOG", "NFLX", "TSLA"])
    ticker = "AAPL"

    while True:
        # Generate quotes
        # Generate orders
        # Generate macro events
        # Generate stock price movement
        # Simulate mm behavior

        latest_data = mb.generate_market_tick(latest_data)
        new_quote = market_maker.quote(ticker, latest_data)
        new_order = ib.order(ticker, latest_data)

        AAPL_order_book.handle_quote(new_quote)
        AAPL_order_book.handle_order(new_order)

        print(new_quote)
        print(new_order)

        time.sleep(1)

if __name__ == "__main__":
    print(run_simulation())