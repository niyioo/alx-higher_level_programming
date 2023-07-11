#!/usr/bin/python3
""" Module for class MyInt """


class MyInt(int):
    """
    A class representing a rebel integer.
    """

    def __eq__(self, other):
        """
        Overrides the equality operator.

        Args:
            other: The object to compare against.

        Returns:
            True if the values are not equal, False otherwise.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Overrides the inequality operator.

        Args:
            other: The object to compare against.

        Returns:
            True if the values are equal, False otherwise.
        """
        return super().__eq__(other)
