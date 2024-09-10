#!/usr/bin/python3
for number_1 in range(0, 10):
    for number_2 in range(number_1 + 1, 10):
        print("{}{}".format(number_1, number_2),
              end="\n" if number_1 == 8 and number_2 == 9 else ", ")
