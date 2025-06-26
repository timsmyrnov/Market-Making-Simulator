import random

def generate_market_tick(curr_prices: dict, mu=0.0001, sigma=0.003):
    new_prices = curr_prices.copy()

    for sym in new_prices:
        # Geometric Brownian motion
        new_prices[sym] *= (1 + random.gauss(mu, sigma))

    return new_prices