def sentinel():
    total = 0
    counter = 0

    grade = int(input("Enter your grade or -1 to quit:"))

    while grade != -1:
        grade = int(input("Enter your grade or -1 to quit:"))
        total += grade
        counter += 1
    print(total)

    if counter != 0:
        average = total / counter
        print(f'class average is {average}')

    else:
        print("No grades were entered!")


def count_result():
    passes = 0
    failures = 0

    for _ in range(10):
        result = int(input("Enter result (1=pass, 2=fail):"))
        if result == 1:
            passes += 1
        else:
            failures += 1
    print(f"Number of pass is {passes}")
    print(f"Number of failures is {failures}")



sentinel()
count_result()
