# class Spacecraft():
#     def __init__(self, name, fuel_level, fuel_efficiency):
    
#         self.name = name
#         self.fuel_level = fuel_level
#         self.fuel_efficiency = fuel_efficiency

#     def add_fuel(self, amount):
#         self.fuel_level += amount

#     def calculate_fuel(self, distance):
#         return distance / self.fuel_efficiency
    
#     def check_fuel(self, distance):
#         return self.fuel_level >= self.calculate_fuel(distance)

#     def launch(self, distance):
#         if self.check_fuel(distance):
#             self.fuel_level -= self.calculate_fuel(distance)
#             print(f"{self.name} has successfully traveled {distance} units!")
#         else:
#             print(f"{self.name} lacks the required fuel to travel {distance} units.")
 

# voyager = Spacecraft("Voyager", 2000, 1)
# print(voyager.calculate_fuel(100))  
# print(voyager.check_fuel(1000))              
# voyager.launch(500)                          
# print(voyager.fuel_level) 

class Planet():
    def __init__(self, name, coordinates, danger, resources, atmosphere):
        self.name = name
        self.coordinates = coordinates
        self.danger = danger
        self.resources = resources
        self.atmossphere = atmosphere

    def __str__(self):
        return f"{self.name} is located at {self.coordinates} with {self.danger} of mission success and {self.resources} value. It has {self.atmossphere}"

    # def __sub__(self, other):


p1 = Planet("Mars", (150, 0, 0), "low probability", "high reward", "very little oxygen")

p2 = Planet("Earth", (227, 0, 1), "high probability", "moderate reward", "moderate amounts of oxygen")

print(p1)
print(p2)
        