#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            result = 0
            if i < len(my_list_1) and i < len(my_list_2):
                try:
                    numerator = float(my_list_1[i])
                    denominator = float(my_list_2[i])
                    if denominator != 0:
                        result = numerator / denominator
                    else:
                        print("division by 0")
                except (ValueError, TypeError):
                    print("wrong type")
            else:
                print("out of range")
        except IndexError:
            pass
        finally:
            new_list.append(result)
    return new_list
