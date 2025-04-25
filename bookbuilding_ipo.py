from collections import namedtuple, defaultdict

Bid = namedtuple('Bid', ['price', 'volume'])

# List of individual bids (unsorted)
individual_bids = [
    Bid(10, 2_000),
    Bid(12, 1_000),
    Bid(11, 1_000),
    Bid(13, 500),
    Bid(12, 2_000),
    Bid(14, 1_000),
    Bid(10, 3_000),
    Bid(9, 2_000),
    Bid(8, 6_000),
    Bid(11, 3_000),
]

# 1. Aggregate into price levels
def build_cumulative_bids(individual_bids):
    price_to_volume = defaultdict(int)
    for bid in individual_bids:
        price_to_volume[bid.price] += bid.volume

    sorted_prices = sorted(price_to_volume.items(), key=lambda x: -x[0])

    # Compute cumulative volume
    cumulative_bids = []
    cumulative = 0

    for price, volume in sorted_prices:
        cumulative += volume
        cumulative_bids.append(Bid(price, cumulative))

    return cumulative_bids

# Total shares offered
supply=5_000

def maximize_proceeds(cumulative_bids, supply):
    for bid in cumulative_bids:
        if bid.volume >= supply:
            return bid.price, bid.price * supply
        
    return None, 0

def maximize_revenue(cumulative_bids):
    max_revenue = 0
    best_price = None

    for bid in cumulative_bids:
        revenue = bid.price * bid.volume
        if revenue > max_revenue:
            max_revenue = revenue
            best_price = bid.price
        
    return best_price, max_revenue


# Build cumulative
cumulative_bids = build_cumulative_bids(individual_bids)

# Run two strategies
proceeds_price, proceeds_amount = maximize_proceeds(cumulative_bids, supply)
revenue_price, revenue_amount = maximize_revenue(cumulative_bids)

print("Cumulative Bids:")
for bid in cumulative_bids:
    print(f"Volume: {bid.volume} - Price ${bid.price}")

print("\nMaximize Proceeds Strategy:")
print(f"  IPO Price: ${proceeds_price}")
print(f"  Total Proceeds: ${proceeds_amount:,.0f}")

print("\nMaximize Revenue Strategy:")
print(f"  Optimal Price: ${revenue_price}")
print(f"  Revenue (hypothetical full fill): ${revenue_amount:,.0f}")

