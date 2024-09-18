#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return (0)

    total_weight = 0
    size = 0
    for tup in my_list:
        total_weight += (tup[0] * tup[1])
        size += (tup[1])
    return (total_weight / size)
