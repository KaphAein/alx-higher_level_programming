#!/usr/bin/python3
def best_score(a_dictionary):
    max_value = 0
    if a_dictionary is None:
        return None
    for key, value in a_dictionary.items():
        if value > max_value or max_value is None:
            max_value = value
    return max_value
