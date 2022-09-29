#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new_dic = a_dictionary
    [print("%s: %s" % (i, new_dic[i])) for i in sorted(new_dic.keys())]
