def contains_duplicate(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    return False if sorted(nums) == sorted(list(set(nums))) else True


# ------------- TESTS -------------- #
# should be True
print(contains_duplicate([1, 2, 3, 1]))
print(contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
# should be False
print(contains_duplicate([1, 2, 3, 4]))
print(contains_duplicate([1]))
print(contains_duplicate([3, 1]))
print(contains_duplicate([1, 5, -2, -4, 0]))

