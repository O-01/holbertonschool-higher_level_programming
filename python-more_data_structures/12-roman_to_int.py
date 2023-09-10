#!/usr/bin/python3
def roman_to_int(roman_string):
    total = 0
    if roman_string and isinstance(roman_string, str):
        roman_dict = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400,
                      'C': 100, 'XC': 90, 'L': 50, 'XL': 40,
                      'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}

        add_prev = 0
        for i, n in enumerate(roman_string):
            if add_prev == 1:
                total += roman_dict[roman_string[i - 1] + n]
                add_prev = 0
                continue
            else:
                if i == len(roman_string) - 1:
                    if n in roman_dict:
                        total += roman_dict[n]
                elif i < len(roman_string) - 1:
                    if n + roman_string[i + 1] in roman_dict:
                        add_prev = 1
                        continue
                    elif n in roman_dict:
                        total += roman_dict[n]
    return total
