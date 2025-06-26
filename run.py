import time
import random
import yfinance as yf
import fetch_market_data as fmd
import order_book as ob
import market_behavior as mb
import investor_behavior as ib
import market_maker as mm

def run_simulation():
    order_book = ob.OrderBook()
    market_maker = mm.MarketMaker()
    latest_data = fmd.download_latest_data(["AAPL", "MSFT", "GOOG", "NFLX", "TSLA"])

    while True:
        # Generate quotes
        # Generate offers
        # Generate macro events
        # Generate stock price movement
        # Simulate mm behavior

        latest_data = mb.generate_market_tick(latest_data)
        new_quote = market_maker.quote("AAPL", latest_data)
        order_book.handle_quote(new_quote)
        print(new_quote, round(latest_data["AAPL"], 2))

        time.sleep(0.05)

if __name__ == "__main__":
    print(run_simulation())