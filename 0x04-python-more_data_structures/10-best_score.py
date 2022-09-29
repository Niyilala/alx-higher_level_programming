#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    max_val = max(a_dictionary.values())
    for i, j in a_dictionary.items():
        if max_val == j:
            return (i)
