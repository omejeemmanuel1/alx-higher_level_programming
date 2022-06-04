#!/usr/bin/python3

<<<<<<< HEAD
=======

def new_in_list(my_list, idx, element):
    """Replace an element in a copied list at a specific position."""
    if idx < 0 or idx > (len(my_list) - 1):
        return (my_list)
>>>>>>> 6c6b6fdcbe5ac6a607b9e7822bdc0c64dbc99b1b

def no_c(my_string):
    """Remove all characters c and C from a string."""
    copy = [x for x in my_string if x != 'c' and x != 'C']
    return ("".join(copy))
