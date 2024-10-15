#!/usr/bin/python3
"""
log_parser module.

A script for parsing and analyzing log data from standard input.
"""


def print_line(size: int, status_codes: dict) -> None:
    """
    Print the file size and counts of specific HTTP status codes.

    Args:
        size (int): The size of the file.
        status_codes (dict): A dictionary containing the counts\
            of specific HTTP status codes.
    """
    print("File size: {}".format(size))
    for k, v in sorted(status_codes.items()):
        if v > 0:
            print("{}: {}".format(k, v))
    pass


if __name__ == "__main__":
    from sys import stdin

    status_codes = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0
        }
    size = count = 0

    try:
        for line in stdin:
            splited_line = line.split()
            if len(splited_line) >= 2:
                status = splited_line[-2]
                size += int(splited_line[-1])
                if status in status_codes:
                    status_codes[status] += 1
            count += 1
            if count % 10 == 0:
                print_line(size, status_codes)
        print_line(size, status_codes)
    except KeyboardInterrupt as e:
        print_line(size, status_codes)
