numbers = [13, 4, 6, 9, 3]
print('\nCreating a bar chart from numbers:')
print(f'Index{"Value":>10} Bar')
for index, value in enumerate(numbers):
    print(f' {index :> 5} {value:>5}    {"*" * value}')
