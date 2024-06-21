import sys
from datetime import datetime
from datetime import timedelta

print(datetime.now() + timedelta(days=1))
print(datetime.now() + timedelta(seconds=60))
print(datetime.now() + timedelta(days=365 * 2))

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 6:
        date, time, store, item, cost, payment = data
        print('{0}\t{1}'.format(item, cost))

delta = timedelta(days=100, hours=10, minutes=13)
print(delta)


def process_measurement(feet, inches):
    current_time = datetime.now()
    print("Feet: {0}, Inches: {1}, Time: {2}".format(feet, inches, current_time))
