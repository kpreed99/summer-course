# import random

# with open('writeint.txt', 'w') as file:
#     for line in range(100):
#         random_number = random.randint(1, 1001)
#         file.write(str(random_number) + "\n")

with open('writeint.txt', 'r') as file:
    lines = file.readlines()

numbers = []

for line in lines:
    numbers.append(int(line.strip()))

highest = max(numbers)
lowest = min(numbers)
average = sum(numbers) / len(numbers)

print("Highest:", highest)
print("Lowest:", lowest)
print("Average:", average)