#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    results = []
    for num in my_list:
        results.append(num % 2 == 0)
    return results
