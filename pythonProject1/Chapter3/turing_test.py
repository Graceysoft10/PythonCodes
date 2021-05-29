for _ in range(2):
    prompt1 = input("What is your problem?")
    prompt2 = input("Have you had this problem before?(yes/no)")
    if prompt2.__eq__("yes"):
        print("Well,you have it again")
        print()
    else:
        print("Well,you have it now")
        print()