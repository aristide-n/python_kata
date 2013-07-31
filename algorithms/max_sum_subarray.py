__author__ = 'Aristide'

# Three algorithms that solves the problem f finding the sub-array with the maximum sum in an array of integers


#===========================================================================================
# The first algorithm executes in O(n) time

def find_max_subarray_n(array):
    """
    Return a tuple of the beginning and the end index of the subarray, in that order
    Doctests:
        >>> find_max_subarray_n([5, -10, 4, 3, 2, 0, 1, -3, 7])
        (2, 8)

        >>> find_max_subarray_n([-5, -10, 4, 3, 2, 0, 1, -3, 7])
        (2, 8)

        >>> find_max_subarray_n2([-5, -10, 4, 3, 2, 0, 1, -3, 7, 0, -6])
        (2, 9)

        >>> find_max_subarray_n([-5, -40, -4, -3, -2, -1, -3, -7])
        (5, 5)

    """

    subarray_beginning = 0;
    temp_subarray_beginning = 0;
    subarray_end = 0;

    max_sum_so_far = array[0];
    max_sum_ending_here = 0;

    for i in range(len(array)):
        if max_sum_ending_here < 0:
            max_sum_ending_here = array[i]
            temp_subarray_beginning = i
        else:
            max_sum_ending_here += array[i]

        if max_sum_ending_here >= max_sum_so_far:
            max_sum_so_far = max_sum_ending_here
            subarray_beginning = temp_subarray_beginning
            subarray_end = i

    return (subarray_beginning, subarray_end)



#===========================================================================================
# The second algorithm is the (good) old brute force. It executes in O(n^2) time

def find_max_subarray_n2(array):
    """
    Return a tuple of the beginning and the end index of the subarray, in that order
    Doctests:
        >>> find_max_subarray_n2([5, -10, 4, 3, 2, 0, 1, -3, 7])
        (2, 8)

        >>> find_max_subarray_n2([-5, -10, 4, 3, 2, 0, 1, -3, 7])
        (2, 8)

        >>> find_max_subarray_n2([-5, -10, 4, 3, 2, 0, 1, -3, 7, 0, -6])
        (2, 9)

        >>> find_max_subarray_n2([-5, -40, -4, -3, -2, -1, -3, -7])
        (5, 5)

    """

    subarray_beginning = 0
    subarray_end = 0
    max_sum = array[0]

    for i in range(len(array)):
        temp_sum = 0

        for j in range(i, len(array)):
            temp_sum += array[j]

            if temp_sum >= max_sum:
                max_sum = temp_sum

                subarray_beginning = i
                subarray_end = j

    return (subarray_beginning, subarray_end)



if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
