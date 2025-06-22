import yfinance as yf
import fetch_market_data as fmd

def run_simulation():
    latest_data = fmd.download_latest_data(["AAPL", "MSFT", "GOOG", "NFLX", "TSLA"])
    return latest_data

if __name__ == "__main__":
    print(run_simulation())