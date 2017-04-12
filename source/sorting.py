#!python

def bubble_sort(elements):
    for i in xrange(len(elements) - 1):
        for j in xrange(len(elements) - 1):
            if elements[j] > elements[j+1]:
                elements[j], elements[j+1] = elements[j+1], elements[j]
    return elements

def main():
    elements = [3, 6, 2, 4, 9, 1, 5, 7, 8]
    print bubble_sort(elements)

if __name__ == '__main__':
    main()
