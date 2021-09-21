def calculate_product(*numbers):
    product = 1
    for number in numbers:
        product *= number

    return product


print(calculate_product(12, 23, 10, 33, 5, 3, 2, 1, 8))
