#!/usr/bin/python3
""" Module for log parsing """


import sys


def print_info():
    """
    Prints the file size and status code counts.
    """
    print('File size: {:d}'.format(file_size))

    for scode, code_times in sorted(status_codes.items()):
        if code_times > 0:
            print('{}: {:d}'.format(scode, code_times))


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

lc = 0
file_size = 0

try:
    for line in sys.stdin:
        if lc != 0 and lc % 10 == 0:
            print_info()

        pieces = line.split()

        try:
            status = pieces[-2]

            if status in status_codes:
                status_codes[status] += 1
        except IndexError:
            pass

        try:
            file_size += int(pieces[-1])
        except (IndexError, ValueError):
            pass

        lc += 1

    print_info()
except KeyboardInterrupt:
    print_info()
    raise
