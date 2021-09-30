numbers = [13, 4, 6, 9, 3]
print('\nCreating a bar chart from numbers:')
print(f'Index{"Value":>10} Bar')
for index, value in enumerate(numbers):
    print(f' {index :> 5} {value:>5}    {"*" * value}')

numbers2 = list(range(1, 16))
print(numbers2)
ev = numbers2[1:len(numbers2):2]
print(ev)
numbers2[5:10] = [0] * len(numbers2[5:10])

print(numbers2)
numbers2[5:] = []
print(numbers2)
