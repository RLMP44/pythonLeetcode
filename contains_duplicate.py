def contains_duplicate(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    reversed_nums = nums.reverse()
    if nums == list(set(nums)) or reversed_nums == list(set(nums)):
        return False
    else:
        return True


# ------------- TESTS -------------- #
# should be True
print(contains_duplicate([1, 2, 3, 1]))
print(contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
# should be False
print(contains_duplicate([1, 2, 3, 4]))
print(contains_duplicate([1]))
print(contains_duplicate([3, 1]))

