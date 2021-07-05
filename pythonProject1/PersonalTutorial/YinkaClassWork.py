def check_vowels(user_input):
    is_Contained = False
    vowels = ['a', 'e', 'i', 'o', 'u']
    for i in user_input:
        if i in vowels:
            is_Contained = True
            break

    if is_Contained:
        print("contains vowels!")
    else:
        print("Does not contain vowels!")


from_user = input("Enter a word")
check_vowels(from_user)


def check_if_odd_or_even(user_Number):
    if user_Number % 2 == 0:
        print(user_Number, "is Even Number")
    else:
        print(user_Number, "is Odd Number")


userNumber = int(input("Enter a number"))
check_if_odd_or_even(userNumber)


def sort_even_and_odd_numbers_respectively(list_of_integer):
    even = []
    odd = []
    for x in list_of_integer:
        if x % 2 == 0:
            even.append(x)
        else:
            odd.append(x)

    even.sort()
    odd.sort()
    for i in odd:
        even.append(i)

    return even


print("numbers sort in even and odd respectively.")
list = [2, 3, 4, 5, 6]
print(sort_even_and_odd_numbers_respectively(list))
