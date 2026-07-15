# for number in range(1, 101):
#     if number % (3 and 5) == 0:
#         print(number, "FizzBuzz")
#     elif number % 3 == 0:
#         print(number, "Fizz")
#     elif number % 5 == 0:
#         print(number, "Buzz")
#     else:
#         print(number)

# user_select = input("Please pick rock, paper, or scissors: ")
# computer_select = "rock" 

# if user_select == "rock" and computer_select == "paper":
#         print("You lose")
# if user_select == "rock" and computer_select == "paper":
#         print("You lose")
# if user_select == "rock" and computer_select == "paper":
#         print("You lose")
# if user_select == "rock" and computer_select == "paper":
#         print("You lose")
# if user_select == "rock" and computer_select == "paper":
#         print("You lose")
# if user_select == "rock" and computer_select == "paper":
#         print("You lose")
# if user_select == "rock" and computer_select == "paper":
#         print("You lose")
# else:
#         print("You tie")

# import random

# secret_num = random.randint(1, 100)
# user_guess = int(input("Guess the secret number(1-100): "))
# while user_guess != secret_num:
#     if user_guess < secret_num:
#         print("too low")
#     else:
#         print("too high")   
#     user_guess = int(input("Guess the secret number(1-100): ")) 
    
# print(f"Congrats, you got it {secret_num}")

# import random

# random_num = random.randint(0, 101)
# if random_num < 50:
#     print("The number is less than 50")
# elif random_num > 50:
#     print("The number is grater than 50")
# else:
#     print("The number is 50")
# print (random_num)

# def area(length, width):
#     return(length * width)

# user_length = int(input("Length:")) 
# user_width = int(input("Width:"))
# area_of_sq = area(user_length, user_width)

# print(area_of_sq)

# def tip(total, percentage):
#     percent_conv = percentage / 100
#     return(total*percent_conv)

# user_total = float(input("Total Bill: "))
# user_percentage = float(input("Percentage you want to tip: "))

# user_tip = tip(user_total, user_percentage)

# print(user_tip)

def char_count(str1, str2):
    length1 = len(str1)
    length2 = len(str2)
    if length1 < length2:
        return(str2)
    elif length2 <length1:
        return(str1)
    else:
        return("They are equal")

string1 = str(input("Enter a statement: "))
string2 = str(input("Enter a second statement: "))

str_count = char_count(string1, string2)

print(str_count)