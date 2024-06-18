import sys
from datetime import datetime
from datetime import timedelta
# Iterate over each line provided through standard input
for line in sys.stdin:
    # Strip leading/trailing whitespace and split the line into a list based on tab delimiter
    data = line.strip().split("\t")

    # Check if the split list has exactly six elements
    if len(data) ==6:
        # Unpack the list into variables
        date, time, store, item, cost, payment = data

        # Get the current time
        now = datetime.now()
        current_time = now.strftime("%Y-%m-%d %H:%M:%S")

        # Print the item and cost, along with the current time
        print(f"{item}\t{cost}\t{current_time}")