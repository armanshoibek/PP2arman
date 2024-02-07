def spy_game(nums):
    seen_zero = False
    seen_double_zero = False

    for num in nums:
        if num == 0:
            if seen_zero:
                seen_double_zero = True
            seen_zero = True
        elif num == 7:
            if seen_double_zero:
                return True

    return False

print(spy_game([1, 2, 4, 0, 0, 7, 5]))  # Output: True
print(spy_game([1, 0, 2, 4, 0, 5, 7]))  # Output: True
print(spy_game([1, 7, 2, 0, 4, 5, 0]))  # Output: False
