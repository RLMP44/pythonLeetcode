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


# ---------- TESTS ----------- #
# all should return True
print(roman_to_int('III') == 3)
print(roman_to_int('LVIII') == 58)
print(roman_to_int('MCMXCIV') == 1994)
print(roman_to_int('CMLIV') == 954)
print(roman_to_int('CCCLXII') == 362)

