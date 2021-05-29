def find_pythagorean_triple(a, b, c):
    first = a * a
    second = b * b
    third = c * c

    if first + second == third:
        print("This is a pythagorean triple")
    else:
        print("Not a pythagorean triple")


def find_list_of_pythagorean_triple():
    list = []
    for a in range(1, 30):
        for b in range(1, 30):
            for c in range(1, 30):
                if (a * a) + (b * b) == c * c:
                    # print(c,b,a)
                    temp = [a, b, c]
                    list.append(temp)
                    print(list)


find_list_of_pythagorean_triple()
find_pythagorean_triple(3, 4, 5)
