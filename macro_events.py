import random

# "Event": Magnitude

positive_events = {
    "optimism_spike": 0.31,
    "strong_earnings": 0.62,
    "technology_breakthrough": 0.79,
    "favorable_policy_announcement": 0.53,
    "peace_agreement": 0.95,
    "trade_deal_signed": 0.72,
    "stimulus_package": 0.98,
    "rate_cut": 0.61,
    "economic_growth_surprise": 0.69,
    "successful_product_launch": 0.43
}

negative_events = {
    "pessimism_spike": 0.20,
    "irrational_fears": 0.21,
    "recession_fears": 0.70,
    "war_fears": 0.99,
    "trade_policy_issues": 0.50,
    "mass_protests": 0.32,
    "natural_disaster": 0.6,
    "company_crisis": 0.59,
    "company_collapse": 0.88
}

def generate_positive_event():
    return random.choices(list(positive_events.keys()), weights=[1 - v for v in positive_events.values()], k=1)[0]

def generate_negative_event():
    return random.choices(list(negative_events.keys()), weights=[1 - v for v in negative_events.values()], k=1)[0]

def event_probabilities():
    def compute_probs(event_dict):
        weights = [1 - v for v in event_dict.values()]
        total_weight = sum(weights)
        return {
            event: (weight / total_weight)
            for event, weight in zip(event_dict.keys(), weights)
        }

    pos_probs = compute_probs(positive_events)
    neg_probs = compute_probs(negative_events)

    print("\nPositive Events Probabilities:\n")
    for event, prob in sorted(pos_probs.items(), key=lambda x: -x[1]):
        print(f"  {event:30s} \033[92m{prob:.2%}\033[0m")

    print("\nNegative Events Probabilities:\n")
    for event, prob in sorted(neg_probs.items(), key=lambda x: -x[1]):
        print(f"  {event:30s} \033[91m{prob:.2%}\033[0m")

if __name__ == "__main__":
    event_probabilities()