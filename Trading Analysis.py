import csv
from collections import defaultdict
import math

def process_trades(input_file, output_file):
    trade_data = defaultdict(lambda: {"max_gap": 0, "total_volume": 0, "weighted_price_sum": 0, "total_quantity": 0, "max_price": 0, "last_timestamp": None})
    
    with open(input_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            timestamp, symbol, quantity, price = int(row[0]), row[1], int(row[2]), int(row[3])
            
            # Calculate max time gap
            if trade_data[symbol]["last_timestamp"] is not None:
                time_gap = timestamp - trade_data[symbol]["last_timestamp"]
                trade_data[symbol]["max_gap"] = max(trade_data[symbol]["max_gap"], time_gap)
            
            # Update last timestamp
            trade_data[symbol]["last_timestamp"] = timestamp
            
            # Update total volume
            trade_data[symbol]["total_volume"] += quantity
            
            # Update weighted price sum
            trade_data[symbol]["weighted_price_sum"] += quantity * price
            trade_data[symbol]["total_quantity"] += quantity
            
            # Update max price
            trade_data[symbol]["max_price"] = max(trade_data[symbol]["max_price"], price)
    
    # Write output
    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        for symbol in sorted(trade_data.keys()):
            max_time_gap = trade_data[symbol]["max_gap"]
            total_volume = trade_data[symbol]["total_volume"]
            weighted_avg_price = math.trunc(trade_data[symbol]["weighted_price_sum"] / trade_data[symbol]["total_quantity"])
            max_price = trade_data[symbol]["max_price"]
            writer.writerow([symbol, max_time_gap, total_volume, weighted_avg_price, max_price])

# Run the script
input_path = "/Users/vanessali/Desktop/l/CodeExercise/Tests/input_1.csv"
output_path = "/Users/vanessali/Desktop/l/CodeExercise/Tests/output.csv"
process_trades(input_path, output_path)

cd /Users/vanessali/Desktop/l/CodeExercise/Tests
