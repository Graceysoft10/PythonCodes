import random


def fast_plod():
    pass


def slip():
    pass


def slow_pod():
    pass


def generate_percentage_for_tortoise():
    t_percentage = random.randrange(1, 11)
    if 1 <= t_percentage <= 5:
        fast_plod()
    elif 6 <= t_percentage <= 7:
        slip()
    elif 8 <= t_percentage <= 10:
        slow_pod()
    else:
        pass


def generate_percentage_for_hare():
    h_percentage = random.randrange(1, 11)
    print(h_percentage)


def display_position_line():
    i = 0
    while i < 70:
        print("T")
        i += 1



display_position_line()
