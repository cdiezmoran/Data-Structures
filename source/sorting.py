#!python

def bubble_sort(elements):
    for i in xrange(len(elements) - 1):
        for j in xrange(len(elements) - 1):
            if elements[j] > elements[j+1]:
                elements[j], elements[j+1] = elements[j+1], elements[j]
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

def main():
    elements = [3, 6, 2, 4, 9, 1, 5, 7, 8]
    bubble = bubble_sort(elements)
    print bubble

    elements = [3, 6, 2, 4, 9, 1, 5, 7, 8]
    selection = selection_sort(elements)
    print selection

    elements = [3, 6, 2, 4, 9, 1, 5, 7, 8]
    insertion = insertion_sort(elements)
    print insertion

if __name__ == '__main__':
    main()