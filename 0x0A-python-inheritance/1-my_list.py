#!/usr/bin/python3
""" Module for list """


class MyList(list):
    """
    A subclass of list that provides additional functionality.

    """

    def print_sorted(self):
        """
        Prints the list in ascending order.

        """
        sorted_list = sorted(self)
        print(sorted_list)
