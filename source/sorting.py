#!python

def bubble_sort(elements):
    for i in xrange(len(elements) - 1):
        for j in xrange(len(elements) - 1):
            if elements[j] > elements[j+1]:
                elements[j], elements[j+1] = elements[j+1], elements[j]
    return elements

def selection_sort(elements):
    min_number = 0
    min_i = 0
    swap_i = 0

    for i in xrange(len(elements)):
        for j in xrange(swap_i, len(elements)):
            if elements[j] < min_number:
                min_number = elements[j]
                min_i = j
        if swap_i != min_i:
            elements[swap_i], elements[min_i] = elements[min_i], elements[swap_i]
            swap_i += 1
    return elements

def main():
    elements = [3, 6, 2, 4, 9, 1, 5, 7, 8]
    
    bubble = bubble_sort(elements)
    selection = selection_sort(elements)

    print bubble
    print selection

if __name__ == '__main__':
    main()
