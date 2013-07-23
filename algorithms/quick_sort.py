__author__ = 'Aristide'

import sys
import random

count = 0

# Main file to peek at the performance using the total count of comparisons performed during partitioning
def main(argv):
    # List to sort
    my_list = []

    # If the argument is a file name, open the file and place the integer on each line in the list.
    if len(argv) is 1:
        #Open file
        try:
            file = open(argv[0], 'r')
            for line in file:
                my_list.append(int(line))
            file.close()
        except IOError as io_e:
            print "I/O error({0}): {1}".format(io_e.errno, io_e.strerror)
        except EOFError as eof_e:
            print "EOF error({0}): {1}".format(eof_e.errno, eof_e.strerror)
    else:
        print "A file path is required"

    # Sort then print
    sort(my_list, 0, len(my_list) - 1)
    print str(count) + ' comparisons'


def sort(unsorted_list , left_index, right_index):
    """
    Implementation of the quicksort algorithm: http://en.wikipedia.org/wiki/Quicksort

    Doctests:
    >>> my_list = [2, 3, 7, 8, 0, 9, 3, 7, 4, 8, 9]
    >>> sort (my_list, 0, len(my_list) - 1)
    >>> print my_list
    [0, 2, 3, 3, 4, 7, 7, 8, 8, 9, 9]

    >>> my_list = [5, 4, 2, 7, 1, 3]
    >>> sort (my_list, 0, len(my_list) - 1)
    >>> print my_list
    [1, 2, 3, 4, 5, 7]

    >>> my_list = [4, 0, 5, 1]
    >>> sort (my_list, 0, len(my_list) - 1)
    >>> print my_list
    [0, 1, 4, 5]
    """

    # Base case: do nothing for empty or single element lists
    if ((right_index - left_index) > 0):

        global count
        count += right_index - left_index

        # Partition around the pivot
        final_pivot_index = partition(unsorted_list, left_index, right_index)

        # recursively sort the partitions
        sort(unsorted_list, left_index, final_pivot_index-1)

        sort(unsorted_list, final_pivot_index+1, right_index)

    


def partition(unpartitioned_list, left_index, right_index):

    #choose_pivot
    initial_pivot_index = choose_pivot(unpartitioned_list, left_index, right_index)

    # Move pivot to front
    if (left_index != initial_pivot_index):
        temp = unpartitioned_list[initial_pivot_index]
        unpartitioned_list[initial_pivot_index] = unpartitioned_list[left_index]
        unpartitioned_list[left_index] = temp
        initial_pivot_index = left_index

    pivot = unpartitioned_list[initial_pivot_index]

    final_pivot_index = initial_pivot_index

    # Make comparisons to swap list elements in a left group of elements smaller than the pivot, and a right group of
    # elements greater than the product
    for index in range(final_pivot_index + 1, right_index + 1):
        if (unpartitioned_list[index] < pivot):
            # Swap
            temp = unpartitioned_list[index]
            unpartitioned_list[index] = unpartitioned_list[final_pivot_index + 1]
            unpartitioned_list[final_pivot_index + 1] = temp

            # Move the pointer to the rightmost element smaller than the pivot
            final_pivot_index += 1

    # At the end swap the pivot and the rightmost element smaller than the pivot
    unpartitioned_list[initial_pivot_index] = unpartitioned_list[final_pivot_index]
    unpartitioned_list[final_pivot_index] = pivot

    # return the pivot index
    return final_pivot_index


def choose_pivot(unpartitioned_list, left_index, right_index):

    # Use Median of three
    middle_index = left_index + ((right_index - left_index) / 2)
    left = unpartitioned_list[left_index]
    middle = unpartitioned_list[middle_index]
    right = unpartitioned_list[right_index]

    median = sum([left, middle, right]) - min(left, middle, right) - max(left, middle, right)
    if left == median:
        pivot_index = left_index
    elif right == median:
        pivot_index = right_index
    else:
        pivot_index = middle_index

    # Use Random pivot
    # pivot_index = random.randint(left_index, right_index)

    return pivot_index

if __name__ == "__main__":
    main(sys.argv[1:])
    # import doctest
    # doctest.testmod(verbose=True)
