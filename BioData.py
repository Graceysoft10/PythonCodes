# Name = input("Enter your Name: ")
# Age = input("Enter Your Age: ")
# Name2 = input("Enter your Name: ")
# Age2 = input("Enter Your Age: ")
# Name3 = input("Enter your Name: ")
# Age3 = input("Enter Your Age: ")
# Data1 = {Name: Age}
# Data2 = {Name2: Age2}
# Data3 = {Name3: Age3}
# print("First user is ", Data1, "\n" "Second user is", Data2, "\n" "Third user is", Data3)


list = []
i = 0
while i < 3:
    name = input("Enter your name")
    age = input("Enter your age")
    gender = input("Enter your gender")
    tuple_item = name, age, gender
    list.append(tuple_item)
    i += 1

print(list)

