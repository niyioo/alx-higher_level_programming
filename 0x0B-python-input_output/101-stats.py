#!/usr/bin/python3
""" Module for log parsing """


import sys


status_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
total_file_size = 0
status_counts = {code: 0 for code in status_codes}

line_count = 0
try:
    for line in sys.stdin:
        line_count += 1

        """Extract information from the line"""
        line_parts = line.split(' ')
        if len(line_parts) >= 7:
            status_code = line_parts[-2]
            file_size = int(line_parts[-1])
            total_file_size += file_size

            """Count status codes"""
            if status_code in status_counts:
                status_counts[status_code] += 1

        """Print statistics every 10 lines"""
        if line_count % 10 == 0:
            print("File size: {:d}".format(total_file_size))
            for code in sorted(status_counts.keys()):
                if status_counts[code] > 0:
                    print("{:s}: {:d}".format(code, status_counts[code]))

except KeyboardInterrupt:
    """Print final statistics on keyboard interruption"""
    print("File size: {:d}".format(total_file_size))
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print("{:s}: {:d}".format(code, status_counts[code]))
