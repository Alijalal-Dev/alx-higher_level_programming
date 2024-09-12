#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv
    num_args = len(argv) - 1

    if num_args == 0:
        print(f"{num_args} arguments.")
    elif num_args == 1:
        print(f"{num_args} argument:")
    else:
        print(f"{num_args} arguments:")

    for i in range(1, len(argv)):
        print(f"{i}: {argv[i]}")
