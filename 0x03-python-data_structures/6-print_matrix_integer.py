#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for num in range(len(matrix)):
        for no in range(len(matrix[i])):
            if no != 0:
                print(" ", end='')
            print("{:d}".format(matrix[num][no]), end='')
        print()