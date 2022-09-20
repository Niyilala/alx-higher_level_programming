#!/usr/bin/python3
def remove_char_at(str, n):
    string = ""
    j = 0
    for i in str:
        if (j != n):
            string = string + i
        j = j + 1
    return (string)
