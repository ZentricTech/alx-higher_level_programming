#!/usr/bin/python3
"""
Module 1-my_list
class MyList that inherits from list
"""


class MyList(list):
    """
        class that inherits from list
        
        Methods:
        print_sorted(self)
    """


    def print_sorted(self):
        """ print sorted int list in asc order"""
        print(sorted(self))
