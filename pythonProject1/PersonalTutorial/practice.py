numbers = [2, 3, 4, 5, 1, 7, 4, 5, 7, 9]
unique_numbers = []
for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)

print(unique_numbers)

phone = input("Phone :")
digit_mapping = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five"
}
output = ""
for ch in phone:
    output += digit_mapping.get(ch, "!") + " "
print(output)
