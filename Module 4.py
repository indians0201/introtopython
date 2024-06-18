MODULE 4
import math

# coefficients
a = 1
b = -5.86
c = 8.5408

# calculate the discriminant
d = (b**2) - (4*a*c)

# find two solutions
root1 = (-b - math.sqrt(d)) / (2*a)
root2 = (-b + math.sqrt(d)) / (2*a)

print(f"The roots are {root1} and {root2}")

Part 2 Reciprocals
for i in range(2, 11):
    print(f"1/{i} = {1/i}")