#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = 0
    prev_val = 0
    for c in roman_string:
        val = roman_dict.get(c, 0)
        if val == 0:
            return 0
        if val > prev_val:
            num += val - 2 * prev_val
        else:
            num += val
        prev_val = val
    return num
