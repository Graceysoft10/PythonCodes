def eliminate_duplicate(list):
    for i in list:
        for j in list:
            if i == j:
                list.remove(i)

    return list


m = [2, 2, 3, 3, 1, 1, 4, 4]
print(eliminate_duplicate(m))
