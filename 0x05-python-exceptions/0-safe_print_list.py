#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    counter = 0
    for j in range(x):
        try:
            print("{}".format(my_list[j]), end="")
        except IndexError:
            break
        else:
            counter += 1
    print()
    return counter
