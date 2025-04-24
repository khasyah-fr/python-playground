import heapq
import time

class Order:
    def __init__(self, name, order_type, price, quantity, timestamp=time.time()):
        self.name = name
        self.order_type = order_type
        self.price = price
        self.quantity = quantity
        self.timestamp = timestamp

    def __repr__(self):
        return (f"{self.name} {self.order_type.upper()} ${self.price}@{self.quantity:.2f} [t={self.timestamp:.2f}]")
    
class OrderBook:
    def __init__(self):
        self.buy_orders = [] # max-heap: (-price, time, order)
        self.sell_orders = [] # min-heap: (price, time, order)
        self.transactions = []

    def add_order(self, order):
        print(f"New Order: {order}")
        if order.order_type == 'buy':
            heapq.heappush(self.buy_orders, (-order.price, order.timestamp, order))
        else:
            heapq.heappush(self.sell_orders, (order.price, order.timestamp, order))
        self.match_orders()

    def match_orders(self):
        while self.buy_orders and self.sell_orders:
            best_buy = self.buy_orders[0][2]
            best_sell = self.sell_orders[0][2]

            if best_buy.price >= best_sell.price:
                trade_qty = min(best_buy.quantity, best_sell.quantity)
                trade_price = best_sell.price
            
                self.transactions.append({
                    'price': trade_price,
                    'quantity': trade_qty,
                    'buy_name': best_buy.name,
                    'sell_name': best_sell.name,
                    'buy_time': best_buy.timestamp,
                    'sell_time': best_sell.timestamp
                })

                print(f"Trade Executed: {trade_qty} units @ ${trade_price} ({best_buy.name} BUY, {best_sell.name} SELL)")

                best_buy.quantity -= trade_qty
                best_sell.quantity -= trade_qty

                if best_buy.quantity == 0:
                    heapq.heappop(self.buy_orders)
                if best_sell.quantity == 0:
                    heapq.heappop(self.sell_orders)
            else:
                break


    def show_order_book(self):
        print("\n--- ORDER BOOK ---")
        print("Buy Orders:")
        for _, _, o in sorted(self.buy_orders, reverse=True):
            print(o)
        print("Sell Orders:")
        for _, _, o in sorted(self.sell_orders):
            print(o)

    def show_transactions(self):
        print("\n--- TRANSACTIONS ---")
        for tx in self.transactions:
            print(f"{tx['quantity']} @ ${tx['price']} ({tx['buy_name']} BUY, {tx['sell_name']} SELL)")

book = OrderBook()

# Sellers
book.add_order(Order(name='Alice', order_type='sell', price=99, quantity=10))
book.add_order(Order(name='Bob', order_type='sell', price=100, quantity=10))

# Buyers
book.add_order(Order(name='Charlie', order_type='buy', price=100, quantity=15))

# History of transactions
book.show_transactions()

# Order book
book.show_order_book()