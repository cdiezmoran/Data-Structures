import sys

def iterative_factorial(num):
    result = num

    while num > 1:
        num -= 1
        result *= num

    return result

def recursive_linear_search(item, lst, index=0):
    # Base case
    if len(lst) <= 0:
        return False

    if item == lst[0]:
        return index

    return recursive_linear_search(item, lst[1:], (index + 1))

def recursive_binary_search(item, lst, carry=0):
    mid_i = len(lst) / 2

    if item == lst[mid_i]:
        return mid_i + carry

    if len(lst) == 2 and lst[0] != item and lst[1] != item:
        return False

    search = 0
    if item < lst[mid_i]:
        search = recursive_binary_search(item, lst[:mid_i], carry)
    elif item > lst[mid_i]:
        search = recursive_binary_search(item, lst[mid_i:], (carry + mid_i))

    if search is not False:
        return search

    return False

def iterative_binary_search(item, lst):
    carry = 0
    while len(lst) != 2:
        mid_i = len(lst) / 2
        if lst[mid_i] == item:
            return mid_i + carry

        if item < lst[mid_i]:
            lst = lst[:mid_i]
        elif item > lst[mid_i]:
            carry += mid_i
            lst = lst[mid_i:]

    return False

def main():
    num = int(sys.argv[1])
    print "Factorial:", iterative_factorial(num)

    arr = [0, 8, 2, 1, 7, 4]
    print "Recursive Linear Search:", recursive_linear_search(num, arr)

    arr.sort()
    print "Recursive Binary Search", recursive_binary_search(num, arr)

    print "Iterative Binary Search", iterative_binary_search(num, arr)

if __name__ == '__main__':
    main()
