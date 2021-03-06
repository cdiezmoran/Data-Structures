#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return linear_search_recursive(array, item)
    # return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    # TODO: implement linear search recursively here
    if len(array) <= 0:
        return None

    if item == array[0]:
        return index

    return linear_search_recursive(array[1:], item, (index + 1))
    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests below


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return binary_search_iterative(array, item)
    # return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    # TODO: implement binary search iteratively here
    check_i = len(array) / 2
    count = 0
    offset_left = 0
    offset_right = 0
    first_right = False

    while (check_i - offset_right != 1) and (check_i - offset_left != 1) and ((len(array) - 1) - check_i != 1):
        if item == array[check_i]:
            return check_i

        if item < array[check_i]:
            offset_right += check_i
            check_i = (check_i - offset_left) / 2 + offset_left
        elif item > array[check_i]:
            if count == 0:
                first_right = True
            offset_left += check_i - offset_left
            check_i += check_i / 2
            if first_right:
                check_i -= offset_right
        count += 1

    if item == array[check_i]:
        return check_i
    elif item == array[check_i - 1]:
        return check_i - 1
    elif item == array[check_i + 1]:
        return check_i + 1

    return None
    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests below


def binary_search_recursive(array, item, offset=0):
    # TODO: implement binary search recursively here
    mid_i = len(array) / 2

    if item == array[mid_i]:
        return mid_i + offset

    if len(array) == 2:
        if array[0] == item:
            return offset
        elif array[1] == item:
            return offset + 1
        return None

    search = 0
    if item < array[mid_i]:
        search = binary_search_recursive(array[:mid_i], item, offset)
    elif item > array[mid_i]:
        search = binary_search_recursive(array[mid_i:], item, (offset + mid_i))

    return search

    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests below
