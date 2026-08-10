metric_type = input(f"Do you want Miles above Mars or Kilometers above Mars?: ")
# miles_mars = int(input("Enter number of miles: "))
# kilometers_mars = int(input("Enter number of kilometers: "))

if metric_type == "miles above mars":
    miles_mars = int(input("Enter number of miles: "))
    yards = miles_mars * 1760
    feet = miles_mars * 5280
    inches = miles_mars * 63360
    print(f"There are {yards}yds in {miles_mars} miles")
    print(f"There are {feet}ft in {miles_mars} miles")
    print(f"There are {inches}in in {miles_mars} miles")
elif metric_type == "kilometers above mars":
    kilometers_mars = int(input("Enter number of kilometers: "))
    meters = kilometers_mars * 1000
    centimeters = kilometers_mars * 100000
    millimeters = kilometers_mars * 1000000
    print(f"There are {meters}yds in {kilometers_mars} kilometers")
    print(f"There are {centimeters}yds in {kilometers_mars} kilometers")
    print(f"There are {millimeters}yds in {kilometers_mars} kilometers")
else:
    metric_type = input("Do you want Miles above Mars or Kilometers above Mars?: ")


