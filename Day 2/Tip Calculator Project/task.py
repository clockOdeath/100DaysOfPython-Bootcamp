#                               Final - 5 Page
# Tip Calculator Project

# Welcome to the tip calculator!
# What was the total bill?
# How much tip would you like to give? 10, 12, or 15?
# How many people to split the bill?
# Each person should pay: $

print("Welcome to the tip calculator")
bill = float(input("What was the total bill?\n"))
# print(f"Total Bill is = {bill}")

tip = int(input("How much tip would you like to give? 10, 12, or 15?\n"))
# print(f"The tip you want to pay is {tip}")

number_of_people = int(input("How many people to split the bill?\n"))
# print(f"No. of people you want to split are {number_of_people}")

total_bill = bill*(tip/100)+bill    # Percentage: 12%=12/100
print(f"So the bill with tip = {total_bill}")

split_amount = total_bill/number_of_people
final_amount = round(split_amount,2)
print(f"Each person should pay = {final_amount}")




#                                   4 Page

# BMI Calculator
# bmi is equal to the person's weight divided by the person's height squared.
# height = 1.65
# weight = 84
# Calculate the bmi using weight and height.
# bmi = weight/height**2
# or
# bmi = 84 / 1.65 ** 2
# print(bmi)
# print(int(bmi))     #Flooring a No. - last whole no.
# print(round(bmi))   #Rounding a No. rounding to nearest whole no.
# print(round(bmi, 3)) #Rounding with the selected decimal nos.

# Assignment Operators
# score = 0
# score += 5
# score /= 3
# print(score)

# f-strings type f before "" eg - f"" and can add any data type inside curly brackets {}
# age = 39
# height = 5.112
# confirm = False
# print(f"My Age is = {age}, and my height is = {height}, and this info is {confirm}")

#                                   3 Page

# # print("My age: " + str(39))
# # print(111 + 222)
# # print(99 - 9)
# # print(10 * 10)
# # print(5 / 3) # Normal division
# # print(5 // 3)  # // removes anything beyond decimal
# # print(2**3) # exponents 2 to the power
#
# # #PEMDAS - () ** * / + - Left->right
#
# # PAUSE 1. What is the output of this code?
# print(3 * 3 + 3 / 3 - 3)

# PAUSE 2. Change the code so it outputs 3?
#print(3 * 3 + 3 / 3 - 3)
# print(3 * (3 + 3) / 3 - 3) #gg


#                                   2 Page

#len(12345)  #Type Error
#len("Hello")

#Type checking
#print(type("Hello"))    #String
#print(type(1.345))      #Float
#print(type(99))         #Integer
#print(type(True))       #Boolean
#print(type(999_999_888)) #Large Integer

#print("Number of letters in your name: " + len(input("Enter your name"))) # len() will be an int and can be checked using type
# We convert int to str
#print("Number of letters in your name: " + str(len(input("Enter your name"))))


#                                   1 Page
#len("Hello")

#subscripting [0,1,2,3,4] or [-1, -2, -3...]

#print("Mandar"[-4])

#String inside ""
#print("1234" + "2345")

# Integer - whole nos.
#print(123+234)

#Large Integers - print(100_123_345)  100,123,345 is like 100_123_345

#Float - Decimals
#print(2.14)

#Boolean True or False