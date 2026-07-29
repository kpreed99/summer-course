class Spacecraft():
    def __init__(self, name, fuel_level, fuel_efficiency):
    
        self.name = name
        self.fuel_level = fuel_level
        self.fuel_efficiency = fuel_efficiency

    def add_fuel(self, amount):
        self.fuel_level += amount

    def calculate_fuel(self, distance):
        return distance / self.fuel_efficiency
    
    def check_fuel(self, distance):
        return self.fuel_level >= self.calculate_fuel(distance)

    def launch(self, distance):
        if self.check_fuel(distance):
            self.fuel_level -= self.calculate_fuel(distance)
            print(f"{self.name} has successfully traveled {distance} units!")
        else:
            print(f"{self.name} lacks the required fuel to travel {distance} units.")
 

voyager = Spacecraft("Voyager", 2000, 1)
print(voyager.calculate_fuel(100))  
print(voyager.check_fuel(1000))              
voyager.launch(500)                          
print(voyager.fuel_level) 
