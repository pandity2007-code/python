# Find the sum of even numbers from 1 to 100
total = 0

for i in range(2, 101, 2):
    total = total + i

print("Sum =", total)