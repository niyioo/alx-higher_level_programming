#!/usr/bin/python3
""" Module for log parsing """


import sys


def print_info():
    print('File size: {:d}'.format(file_size))

    for scode, code_times in sorted(status_codes.items()):
        if code_times > 0:
            print('{}: {:d}'.format(scode, code_times))

status_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
total_file_size = 0
status_counts = {code: 0 for code in status_codes}

line_count = 0
file_size = 0

try:
    for line in sys.stdin:
        if line_count != 0 and line_count % 10 == 0:
            print_info()

        pieces = line.split()

        try:
            status = int(pieces[-2])

            if str(status) in status_codes.keys():
                status_codes[str(status)] += 1
        except:
            pass

        try:
            file_size += int(pieces[-1])
        except:
            pass

        line_count += 1

    print_info()
except KeyboardInterrupt:
    print_info()
    raise
