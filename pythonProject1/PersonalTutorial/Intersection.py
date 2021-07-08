def find_intersection():
    list = ["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]

    element1 = list[0]
    element2 = list[1]
    element1 = element1.split(", ")
    element2 = element2.split(", ")
    new_value = " "

    for x in element1:

        for y in element2:
            if x == y:
                new_value = new_value + x + ", "


    print(new_value)


find_intersection()
