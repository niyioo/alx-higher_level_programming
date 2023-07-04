#!/usr/bin/python3
""" module LockedClass """


class LockedClass:
    """
    Class that prevents the dynamic creation of new instance attributes,
    except for 'first_name'.
    """
    __slots__ = ["first_name"]
