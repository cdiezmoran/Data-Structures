#!python

from binarysearchtree import BinarySearchTree
from heap import MinHeap

def bubble_sort(elements):
    swap = True
    while swap:
        swap = False
        for i in xrange(len(elements) - 1):
            if elements[i] > elements[i+1]:
                elements[i], elements[i+1] = elements[i+1], elements[i]
                swap = True
    return elements

def cocktail_shaker_sort(elements):
    did_swap = True

    while did_swap:
        did_swap = False
        for i in xrange(len(elements) - 2):
            if elements[i] > elements[i+1]:
                elements[i], elements[i+1] = elements[i+1], elements[i]
                did_swap = True

        if did_swap is False:
            break
        did_swap = False
        for i in xrange(len(elements) - 2, 0, -1):
            if elements[i] > elements[i+1]:
                elements[i], elements[i+1] = elements[i+1], elements[i]
                did_swap = True
    return elements

def selection_sort(elements):
    swap_i = 0

    for i in xrange(len(elements)):
        min_item = elements[swap_i]
        min_i = swap_i

        for j in xrange(swap_i, len(elements)):
            if elements[j] < min_item:
                min_item = elements[j]
                min_i = j

        if swap_i != min_i:
            elements[swap_i], elements[min_i] = elements[min_i], elements[swap_i]

        swap_i += 1
    return elements

def insertion_sort(elements):
    for i in xrange(1, len(elements)):
        current = elements[i]
        pos = i

        while pos > 0 and elements[pos - 1] > current:
            elements[pos] = elements[pos - 1]
            pos -= 1

        elements[pos] = current
    return elements

def tree_sort(elements):
    bst = BinarySearchTree(elements)
    return bst.items_in_order()

def merge(list1, list2):
    break_flag = False
    merged = []
    i_left = 0
    i_right = 0

    while break_flag is not True:
        if i_left < len(list1) and i_right < len(list2):
            if list1[i_left] <= list2[i_right]:
                merged.append(list1[i_left])
                i_left += 1
            else:
                merged.append(list2[i_right])
                i_right += 1
        elif len(list1) == i_left:
            for i in xrange(i_right, len(list2)):
                merged.append(list2[i])
            break_flag = True
        elif len(list2) == i_right:
            for i in xrange(i_left, len(list1)):
                merged.append(list1[i])
            break_flag = True

    return merged


def merge_sort_recursive(items):
    if len(items) <= 1:
        return items

    middle = len(items) / 2

    left_sorted = merge_sort_recursive(items[:middle])
    right_sorted = merge_sort_recursive(items[middle:])
    return merge(left_sorted, right_sorted)

def merge_sort(items):
    middle = len(items) / 2

    left = items[:middle]
    right = items[middle:]

    left_sorted = insertion_sort(left)
    right_sorted = insertion_sort(right)

    return merge(left_sorted, right_sorted)


def heap_sort(items):
    heap = MinHeap(items)
    sorted_list = []

    for i in xrange(len(items)):
        sorted_list.append(heap.remove_min())

    return sorted_list

def main():
    elements = [3, 6, 2, 4, 9, 1, 5, 7, 8]
    bubble = bubble_sort(elements)
    print "Bubble: ", bubble

    elements = [3, 6, 2, 4, 9, 1, 5, 7, 8]
    selection = selection_sort(elements)
    print "Selection: ", selection

    elements = [3, 6, 2, 4, 9, 1, 5, 7, 8]
    insertion = insertion_sort(elements)
    print "Insertion: ", insertion

    elements = [3, 6, 2, 4, 9, 1, 5, 7, 8]
    tree_list = tree_sort(elements)
    print "Tree: ", tree_list

    elements = [3, 6, 2, 4, 9, 1, 5, 7, 8]
    cocktail = cocktail_shaker_sort(elements)
    print "Cocktail: ", cocktail

    elements = [3, 6, 2, 4, 9, 1, 5, 7, 8]
    merge_rec = merge_sort_recursive(elements)
    print "Merge_Recursive: ", merge_rec

    elements = [3, 6, 2, 4, 9, 1, 5, 7, 8]
    merge = merge_sort(elements)
    print "Merge_Iterative: ", merge

    elements = [3, 6, 2, 4, 9, 1, 5, 7, 8]
    heap = heap_sort(elements)
    print "Heap: ", heap

if __name__ == '__main__':
    main()
