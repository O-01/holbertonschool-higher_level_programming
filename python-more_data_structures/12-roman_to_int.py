#!/usr/bin/python3
def roman_to_int(roman_string):
    total = 0
    if not roman_string or roman_string is None:
        return total

    roman_dict = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400,
                  'C': 100, 'XC': 90, 'L': 50, 'XL': 40,
                  'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}

    for i, n in enumerate(roman_string):
        if i == 0 and i == len(roman_string) - 1:
            if n in roman_dict:
                total += roman_dict[n]
        elif i < len(roman_string) - 1:
            if n + roman_string[i + 1] not in roman_dict:
                total += roman_dict[n]
            elif n + roman_string[i + 1] in roman_dict:
                total += roman_dict[n + roman_string[i + 1]]
        elif i > 0 and roman_string[i - 1] + n not in roman_dict:
            total += roman_dict[n]
    return total
