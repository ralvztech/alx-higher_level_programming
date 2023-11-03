#!/usr/bin/python3


def new_in_list(my_list, idx, element):

    if (idx < 0) or (idx > (len(my_list)-1)):
        return my_list

    repl_copy = [x for x in my_list]
    repl_copy[idx] = element
    return repl_copy
