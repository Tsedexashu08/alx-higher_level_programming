#!/usr/bin/python3
# 1-my_list.py
# Tsedalu Ashenafi <Tsedexashu08@github.com>
"""Defines an inherited list class MyList."""


class MyList(list):
    """Implements sorted printing for the built-in list class."""

    def print_sorted(self):
        """Print a list in sorted ascending order."""
        print(sorted(self))
