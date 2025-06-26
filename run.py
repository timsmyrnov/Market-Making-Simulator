import yfinance as yf
import fetch_market_data as fmd

def run_simulation():
    latest_data = fmd.download_latest_data(["AAPL", "MSFT", "GOOG", "NFLX", "TSLA"])
    print(latest_data)
    
    while True:
        # generate quotes
        # generate offers
        # generate macro events
        # generate stock price movement
        # simulate mm behavior
        ...

if __name__ == "__main__":
    print(run_simulation())