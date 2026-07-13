# number = int(input("Provide a number: "))

# if(number >= 1):
#     print("positive")
# elif(number == 0):
#     print("zero")
# else:
#     print("negative")

# number = int(input("Provide a number: "))
# if number % 2 == 0:
#     print("The number is even")
# else:
#     print("The number is odd")

# number = int(input("Provide a your age: "))

# if(number < 13):
#     print("Child")
# elif(number <= 19):
#     print("Teenager")
# elif(number <= 64):
#     print("Adult")
# else:
#     print("Senior")

# number = int(input("Provide a number: "))
# number2 = int(input("Provide another number: "))
# if(number < number2):
#     print(number2, "is larger")
# elif(number2 < number):
#     print(number, "is larger")
# else:
#     print("The numbers are equal")

# user_grade = int(input("Provide your numeric grade: "))
# if(user_grade >= 90):
#     print("A")
# elif(user_grade >= 80):
#     print("B")
# elif(user_grade >= 70):
#     print("C")
# elif(user_grade >= 60):
#     print("D")
# else:
#     print("F")

number = int(input("Enter an even number "))
while number %2 != 0:
    print("This is an odd number")
    number = int(input("Enter and even number "))
print ("Good Job, That is an even number!")