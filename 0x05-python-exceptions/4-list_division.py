#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            result = 0
            if i < len(my_list_1) and i < len(my_list_2):
                if isinstance(my_list_1[i], (int, float)) and \
                        isinstance(my_list_2[i], (int, float)):
                    if my_list_2[i] != 0:
                        result = my_list_1[i] / my_list_2[i]
                    else:
                        print("division by 0")
                else:
                    print("wrong type")
            else:
                print("out of range")
            new_list.append(result)
        except IndexError:
            pass
        finally:
            print(result)
    return new_list
