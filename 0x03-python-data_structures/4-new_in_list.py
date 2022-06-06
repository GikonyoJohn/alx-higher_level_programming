#!/usr/bin/python3
def new_in_list(my_list, idx, new_element):
    length = len(my_list)

    new_list = my_list[:]

    if 0 <= idx < length:
        new_list[idx] = new_element

    return (new_list)

my_list = [1, 2, 3, 4, 5]
idx = 3
new_element = 9
new_list = new_in_list(my_list, idx, new_element)

print(new_list)
print(my_list)
