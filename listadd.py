def add_list(arg):
    x=0
    while True:
        if 0 in arg:
            print("Sorry your list contains a zero")
            break
        else:
            print("Awesome, no zeros on your list")
            for i in arg:
                x+=i
        return x
