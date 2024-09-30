def square():
    c = input("Please enter any integer so its square can be printed.\nPress 'x' to exit and close Docker.\n")
    if c == 'x':
        print("Exit python program")
        exit()
    if not c.isnumeric():
        print("Enter either a number for its squared number as result or 'x' to exit.")
        return True

    print("Your result is:\t", int(c) ** 2)
    return True


while square():
    pass
