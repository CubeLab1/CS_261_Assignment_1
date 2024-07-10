# Name: Jesus Martinez
# OSU Email: martjes6@oregonstate.com
# Course: CS261 - Data Structures
# Assignment: 1- Python Review
# Due Date: 7/09/2024
# Description: Review

import random
from static_array import *


# ------------------- PROBLEM 1 - MIN_MAX -----------------------------------

def min_max(arr: StaticArray) -> tuple[int, int]:
    """
    This function returns a tuple with the minimum and maximum values
    of the input StaticArray.
    """
    # Initialize min and max with the first element of the array
    min_val = arr[0]
    max_val = arr[0]

    # Iterate through the array to find the min and max values
    for i in range(1, arr.length()):
        if arr[i] < min_val:
            min_val = arr[i]
        if arr[i] > max_val:
            max_val = arr[i]

    return min_val, max_val


pass


# ------------------- PROBLEM 2 - FIZZ_BUZZ ---------------------------------
def fizz_buzz(arr: StaticArray) -> StaticArray:
    """
    This function receives a StaticArray of integers and returns a new StaticArray object
    with the content modified as follows:
    1) If the number in the original array is divisible by 3, the corresponding element in the
       new array will be the string ‘fizz’.
    2) If the number in the original array is divisible by 5, the corresponding element in the
       new array will be the string ‘buzz’.
    3) If the number in the original array is both a multiple of 3 and a multiple of 5, the
       corresponding element in the new array will be the string ‘fizzbuzz’.
    4) In all other cases, the element in the new array will have the same value as in the
       original array.
    """
    # Create a new StaticArray of the same size as the input array
    new_arr = StaticArray(arr.length())

    # Iterate through the array and apply the FizzBuzz logic
    for i in range(arr.length()):
        value = arr[i]
        if value % 3 == 0 and value % 5 == 0:
            new_arr[i] = 'fizzbuzz'
        elif value % 3 == 0:
            new_arr[i] = 'fizz'
        elif value % 5 == 0:
            new_arr[i] = 'buzz'
        else:
            new_arr[i] = value

    return new_arr


pass


# ------------------- PROBLEM 3 - REVERSE -----------------------------------
def reverse(arr: StaticArray) -> None:
    """
    This function receives a StaticArray and reverses the order of the elements in the
    array in place.
    """
    left = 0
    right = arr.length() - 1

    while left < right:
        # Swap the elements at left and right indices
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1


pass


# ------------------- PROBLEM 4 - ROTATE ------------------------------------
def rotate(arr: StaticArray, steps: int) -> StaticArray:
    """
    This function receives a StaticArray and an integer value (steps). It creates and returns
    a new StaticArray with the elements rotated right (if steps is positive) or left (if steps is
    negative) by the specified number of steps. The original array is not modified.
    """
    n = arr.length()
    new_arr = StaticArray(n)

    # Normalize steps to ensure it's within the bounds of the array length
    steps = steps % n

    for i in range(n):
        new_index = (i + steps) % n
        new_arr[new_index] = arr[i]

    return new_arr


pass


# ------------------- PROBLEM 5 - SA_RANGE ----------------------------------
def sa_range(start: int, end: int) -> StaticArray:
    """
    This function receives two integers, start and end, and returns a StaticArray
    that contains all the consecutive integers between start and end (inclusive).
    """
    # Determine the number of elements in the range
    length = abs(end - start) + 1

    # Create a new StaticArray of the determined length
    arr = StaticArray(length)

    # Fill the array with consecutive integers from start to end
    if start <= end:
        for i in range(length):
            arr[i] = start + i
    else:
        for i in range(length):
            arr[i] = start - i

    return arr


pass


# ------------------- PROBLEM 6 - IS_SORTED ---------------------------------
def is_sorted(arr: StaticArray) -> int:
    """
    This function receives a StaticArray and returns:
    1 if the array is sorted in strictly ascending order.
    -1 if the array is sorted in strictly descending order.
    0 otherwise.
    """
    n = arr.length()

    if n == 1:
        return 1

    ascending = True
    descending = True

    for i in range(1, n):
        if arr[i] > arr[i - 1]:
            descending = False
        if arr[i] < arr[i - 1]:
            ascending = False

    if ascending:
        return 1
    if descending:
        return -1
    return 0

pass


# ------------------- PROBLEM 7 - FIND_MODE -----------------------------------
def find_mode(arr: StaticArray) -> tuple[object, int]:
    """
    This function receives a StaticArray sorted in either non-descending or non-ascending order.
    It returns the mode (the most-occurring element) of the array and its frequency.
    """
    n = arr.length()
    if n == 0:
        return None, 0

    mode = arr[0]
    mode_count = 1

    current_element = arr[0]
    current_count = 1

    for i in range(1, n):
        if arr[i] == current_element:
            current_count += 1
        else:
            if current_count > mode_count:
                mode = current_element
                mode_count = current_count
            current_element = arr[i]
            current_count = 1

    # Final check for the last element sequence
    if current_count > mode_count:
        mode = current_element
        mode_count = current_count

    return mode, mode_count

    pass


# ------------------- PROBLEM 8 - REMOVE_DUPLICATES -------------------------
def remove_duplicates(arr: StaticArray) -> StaticArray:
    """
    This function receives a StaticArray that is already in sorted order, either
    non-descending or non-ascending. It returns a new StaticArray with all duplicate
    values removed. The original array is not modified.
    """
    n = arr.length()
    if n == 0:
        return StaticArray(0)

    # Determine the size of the new array without duplicates
    unique_count = 1
    for i in range(1, n):
        if arr[i] != arr[i - 1]:
            unique_count += 1

    # Create the new array to store unique elements
    new_arr = StaticArray(unique_count)
    new_index = 0
    new_arr[new_index] = arr[0]
    new_index += 1

    # Fill the new array with unique elements
    for i in range(1, n):
        if arr[i] != arr[i - 1]:
            new_arr[new_index] = arr[i]
            new_index += 1

    return new_arr

    pass


# ------------------- PROBLEM 9 - COUNT_SORT --------------------------------
def count_sort(arr: StaticArray) -> StaticArray:
    """
    This function receives a StaticArray and returns a new StaticArray with the same content
    sorted in non-ascending order using the count sort algorithm. The original array is not modified.
    """
    # Determine the range of the input values
    min_val = arr[0]
    max_val = arr[0]
    for i in range(1, arr.length()):
        if arr[i] < min_val:
            min_val = arr[i]
        if arr[i] > max_val:
            max_val = arr[i]

    # Create the count array
    range_of_values = max_val - min_val + 1
    count_arr = [0] * range_of_values

    # Populate the count array
    for i in range(arr.length()):
        count_arr[arr[i] - min_val] += 1

    # Create the output array
    output_arr = StaticArray(arr.length())
    current_index = 0

    # Populate the output array in non-ascending order
    for i in range(range_of_values - 1, -1, -1):
        while count_arr[i] > 0:
            output_arr[current_index] = i + min_val
            current_index += 1
            count_arr[i] -= 1

    return output_arr

    pass


# ------------------- PROBLEM 10 - SORTED SQUARES ---------------------------
def sorted_squares(arr: StaticArray) -> StaticArray:
    """
    This function receives a StaticArray where the elements are in sorted order, and returns a
    new StaticArray with squares of the values from the original array, sorted in non-descending order.
    The original array is not modified.
    """
    n = arr.length()
    result = StaticArray(n)

    left = 0
    right = n - 1
    position = n - 1

    while left <= right:
        left_square = arr[left] * arr[left]
        right_square = arr[right] * arr[right]

        if left_square > right_square:
            result[position] = left_square
            left += 1
        else:
            result[position] = right_square
            right -= 1

        position -= 1

    return result

    pass


if __name__ == "__main__":
    print('\n# min_max example 1')
    arr = StaticArray(5)
    for i, value in enumerate([7, 8, 6, -5, 4]):
        arr[i] = value
    print(arr)
    result = min_max(arr)
    if result:
        print(f"Min: {result[0]: 3}, Max: {result[1]}")
    else:
        print(min_max())

    print('\n# min_max example 2')
    arr = StaticArray(1)
    arr[0] = 100
    print(arr)
    result = min_max(arr)
    if result:
        print(f"Min: {result[0]}, Max: {result[1]}")
    else:
        print(min_max())

    print('\n# min_max example 3')
    test_cases = (
        [3, 3, 3],
        [-10, -30, -5, 0, -10],
        [25, 50, 0, 10],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr)
        result = min_max(arr)
        if result:
            print(f"Min: {result[0]: 3}, Max: {result[1]}")
        else:
            print(min_max())

    print('\n# fizz_buzz example 1')
    source = [_ for _ in range(-5, 20, 4)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr[i] = value
    print(fizz_buzz(arr))
    print(arr)

    print('\n# reverse example 1')
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    reverse(arr)
    print(arr)
    reverse(arr)
    print(arr)

    print('\n# rotate example 1')
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    for steps in [1, 2, 0, -1, -2, 28, -100, 2 ** 28, -2 ** 31]:
        space = " " if steps >= 0 else ""
        print(f"{rotate(arr, steps)} {space}{steps}")
    print(arr)

    print('\n# rotate example 2')
    array_size = 1_000_000
    source = [random.randint(-10 ** 9, 10 ** 9) for _ in range(array_size)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr[i] = value
    print(f'Started rotating large array of {array_size} elements')
    rotate(arr, 3 ** 14)
    rotate(arr, -3 ** 15)
    print(f'Finished rotating large array of {array_size} elements')

    print('\n# sa_range example 1')
    cases = [
        (1, 3), (-1, 2), (0, 0), (0, -3),
        (-95, -89), (-89, -95)
    ]
    for start, end in cases:
        print(f"Start: {start: 4}, End: {end: 4}, {sa_range(start, end)}")

    print('\n# is_sorted example 1')
    test_cases = (
        [-100, -8, 0, 2, 3, 10, 20, 100],
        ['A', 'B', 'Z', 'a', 'z'],
        ['Z', 'T', 'K', 'A', '5'],
        [1, 3, -10, 20, -30, 0],
        [-10, 0, 0, 10, 20, 30],
        [100, 90, 0, -90, -200],
        ['apple']
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        result = is_sorted(arr)
        space = " " if result and result >= 0 else " "
        print(f"Result:{space}{result}, {arr}")

    print('\n# find_mode example 1')
    test_cases = (
        [1, 20, 30, 40, 500, 500, 500],
        [2, 2, 2, 2, 1, 1, 1, 1],
        ["zebra", "sloth", "otter", "otter", "moose", "koala"],
        ["Albania", "Belgium", "Chile", "Denmark", "Egypt", "Fiji"]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        result = find_mode(arr)
        if result:
            print(f"{arr}\nMode: {result[0]}, Frequency: {result[1]}\n")
        else:
            print(find_mode())

    print('# remove_duplicates example 1')
    test_cases = (
        [1], [1, 2], [1, 1, 2], [1, 20, 30, 40, 500, 500, 500],
        [5, 5, 5, 4, 4, 3, 2, 1, 1], [1, 1, 1, 1, 2, 2, 2, 2]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr)
        print(remove_duplicates(arr))
        print(arr)

    print('\n# count_sort example 1')
    test_cases = (
        [1, 2, 4, 3, 5], [5, 4, 3, 2, 1], [0, -5, -3, -4, -2, -1, 0],
        [-3, -2, -1, 0, 1, 2, 3], [1, 2, 3, 4, 3, 2, 1, 5, 5, 2, 3, 1],
        [10100, 10721, 10320, 10998], [-100320, -100450, -100999, -100001],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(f"Before: {arr}")
        result = count_sort(arr)
        print(f"After : {result}")

    print('\n# count_sort example 2')
    array_size = 5_000_000
    min_val = random.randint(-1_000_000_000, 1_000_000_000 - 998)
    max_val = min_val + 998
    case = [random.randint(min_val, max_val) for _ in range(array_size)]
    arr = StaticArray(len(case))
    for i, value in enumerate(case):
        arr[i] = value
    print(f'Started sorting large array of {array_size} elements')
    result = count_sort(arr)
    print(f'Finished sorting large array of {array_size} elements')

    print('\n# sorted_squares example 1')
    test_cases = (
        [1, 2, 3, 4, 5],
        [-5, -4, -3, -2, -1, 0],
        [-3, -2, -2, 0, 1, 2, 3],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(sorted(case)):
            arr[i] = value
        print(arr)
        result = sorted_squares(arr)
        print(result)

    print('\n# sorted_squares example 2')
    array_size = 5_000_000
    case = [random.randint(-10 ** 9, 10 ** 9) for _ in range(array_size)]
    arr = StaticArray(len(case))
    for i, value in enumerate(sorted(case)):
        arr[i] = value
    print(f'Started sorting large array of {array_size} elements')
    result = sorted_squares(arr)
    print(f'Finished sorting large array of {array_size} elements')
