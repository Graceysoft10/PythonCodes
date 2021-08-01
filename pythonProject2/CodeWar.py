list = []
new_list = []


def find_indices_of_two_added_number(list, number):

    for i in list:
        for j in list:
            if list[i] + list[j] == number:
                new_list[0] = i
                new_list[1] = j

    return new_list


list_items = [1, 2, 3, 4, 5]
value = 3
print(find_indices_of_two_added_number(list_items, value))
