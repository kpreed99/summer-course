# import random

# # with open('writeint.txt', 'w') as file:
# #     for line in range(100):
# #         random_number = random.randint(1, 1001)
# #         file.write(str(random_number) + "\n")

# # with open('writeint.txt', 'r') as file:
# #     lines = file.readlines()

# # numbers = []

# # for line in lines:
# #     numbers.append(int(line.strip()))

# # highest = max(numbers)
# # lowest = min(numbers)
# # average = sum(numbers) / len(numbers)

# # print("Highest:", highest)
# # print("Lowest:", lowest)
# # print("Average:", average)

# with open('preclass.txt', 'w') as file:
#     for line in range(100):
#         random_number = random.randint(1, 1001)
#         file.write(str(random_number) + "\n")

# with open('preclass.txt', 'r') as file:
#     lines = file.readlines()

# numbers = []

# for line in lines:
#     numbers.append(int(lines.strip()))
# import math

# print("=" * 3,"PIZZA PARTY PLANNER", "=" * 3)
# guest = int(input("How many guests?: "))
# slices = int(input("How many slices per person?: "))
# pizza_slices = int(input("How many slices per pizza?: "))

# def pizzas_needed(people, slices_per_person, slices_per_pizza):
#     return (people * slices_per_person) / slices_per_pizza
 

# def leftover_slices(people, slices_per_person):
#     slices_needed = people * slices_per_person
#     total_slices = pizzas * pizza_slices
#     return (total_slices - slices_needed)

# pizzas = math.ceil(pizzas_needed(guest, slices, pizza_slices))
# total_slices = pizzas * pizza_slices
# remaining = leftover_slices(guest, slices)

# print("=" * 3,"PARTY SUMMARY", "=" * 3)
# print(f"Guests: {guest}")
# print(f"Pizzas to order: {pizzas}")
# print(f"Total slices: {total_slices}")
# print(f"Leftover slices: {remaining}")