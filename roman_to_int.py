HASH = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}

NEXT = {
    'I': ['V', 'X'],
    'X': ['L', 'C'],
    'C': ['D', 'M']
}


def roman_to_int(s):
    """
    :type s: str
    :rtype: int
    """
    integer = 0
    numerals_list = list(s)
    for index, char in enumerate(numerals_list, start=-1):
        integer += -HASH[char] if need_reduce(char, numerals_list, index) else HASH[char]
    return integer


def need_reduce(char, numerals_list, index):
    return char in NEXT.keys() and numerals_list[index + 1] in NEXT[char]


# ---------- TESTS ----------- #
# all should return True
print(roman_to_int('III') == 3)
print(roman_to_int('LVIII') == 58)
print(roman_to_int('MCMXCIV') == 1994)
print(roman_to_int('CMLIV') == 954)
print(roman_to_int('CCCLXII') == 362)

