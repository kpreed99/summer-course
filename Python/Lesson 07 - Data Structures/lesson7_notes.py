
coordinates = []
with open("preclass_problem1_data.txt", 'r') as file:
   
    for line in file:
        coordinate = int(line)
        coordinates.append(int(line.strip()))

highest = max(range(coordinates), 5)
grid = sum(highest) / len(highest)
print(highest)
print(grid)