def modify_element(items):
    for i in range(len(items)):
        items[i] *= 2


numbers = [10, 2, 5, 7, 8]
modify_element(numbers)
print(numbers)

# Sorting numbers
values = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]
values.sort()
print(values)
values.sort(reverse=True)
print(values)

# sorted functions
ordered_values = sorted(values)
print(ordered_values)
print(values)
values.index(9)

foods = ['Cookies', 'pizza', 'Grapes',
         'apples', 'steak', 'Bacon']
# foods.sort()
new_foods = sorted(foods)
print(foods)
print(new_foods)
foods.index('pizza')