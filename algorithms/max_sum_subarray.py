__author__ = 'Aristide'

# Three algorithms that solves the problem f finding the sub-array with the maximum sum in an array of integers
# http://en.wikipedia.org/wiki/Maximum_subarray_problem


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



#===========================================================================================
# The third algorithm uses the divide and conquer paradigm. It executes in O(nlog(n)) time

def find_max_subarray_nlogn(array):
    """
    Return a tuple of the beginning and the end index of the subarray, in that order

    Doctests:
        >>> find_max_subarray_nlogn([5])
        (0, 0)

        >>> find_max_subarray_nlogn([5, 10])
        (0, 1)

        >>> find_max_subarray_nlogn([-5, -10, -2, -9, -7, -13, 11, -4])
        (6, 6)

        >>> find_max_subarray_nlogn([5, -10, 4, 3, 2, 0, 1, -3, 7])
        (2, 8)

        >>> find_max_subarray_nlogn([-5, -10, 4, 3, 2, 0, 1, -3, 7])
        (2, 8)

        >>> find_max_subarray_nlogn([-5, -10, 4, 3, 2, 0, 1, -3, 7, 0, -6])
        (2, 9)

        >>> find_max_subarray_nlogn([-5, -40, -4, -3, -2, -1, -3, -7])
        (5, 5)

    """
    return find_max_subarray_recursively(array, 0, (len(array) - 1))[0:2]


def find_max_subarray_recursively(array, left_end_index, right_end_index):
    """
    - Partition [in place] the array from the left end to the right end in two, and recurse on the parts.
    - Find the subarray crossing the twoparts having the largest sum
    - Find the subarray having the largest sum among the 3 results

    Return a tuple of the beginning and the end index of the subarray, and the sum of the subarray, in that order
    """

    if left_end_index == right_end_index:
        # Base case
        result = (left_end_index, right_end_index, array[left_end_index])

    else:
        # Divide and Conquer

        # The right end of the left partition is the sum of the left index and the integer division by 2 of the
        # difference between the right end and the left end
        left_max = find_max_subarray_recursively(array, left_end_index, left_end_index +
                                                                        ((right_end_index - left_end_index) / 2))
        #The left end of the right partition is the right end of the left partition
        right_max = find_max_subarray_recursively(array, (left_end_index + ((right_end_index - left_end_index) / 2))
                                                          +1, right_end_index)

        # Combine
        crossing_max_left = find_max_subarray_crossing_to_left(array, left_end_index, left_end_index +
                                                                        ((right_end_index - left_end_index) / 2))
        crossing_max_right = find_max_subarray_crossing_to_right(array, (left_end_index +
                                                                         ((right_end_index - left_end_index) / 2))
                                                                         +1, right_end_index)
        crossing_max = find_max_subarray_crossing(crossing_max_left, crossing_max_right)

        # Find the highest sum among left_max, right_max, and max_crossing
        max_sum = max(left_max[2], right_max[2], crossing_max[2])

        if max_sum == left_max[2]:
            result = left_max
        elif max_sum == right_max[2]:
            result = right_max
        else:
            result = crossing_max

    return result


def find_max_subarray_crossing_to_left(array, left_end_index, right_end_index):
    """
    The end index is the right end.

    Return a tuple of the beginning and the end index of the subarray, and the sum of the subarray, in that order.
    """
    beginning = right_end_index
    max_sum = array[right_end_index]
    running_sum = array[right_end_index]

    for i in range(right_end_index - 1, left_end_index - 1, -1):
        running_sum  += array[i]
        if running_sum >= max_sum:
            max_sum = running_sum
            beginning = i

    return (beginning, right_end_index, max_sum)


def find_max_subarray_crossing_to_right(array, left_end_index, right_end_index):
    """
    The beginning index is the left end.

    Return a tuple of the beginning and the end index of the subarray, and the sum of the subarray, in that order.
    """
    end = left_end_index
    max_sum = array[left_end_index]
    running_sum = array[left_end_index]

    for i in range(left_end_index + 1, right_end_index + 1):
        running_sum  += array[i]
        if running_sum >= max_sum:
            max_sum = running_sum
            end = i

    return (left_end_index, end, max_sum)


def find_max_subarray_crossing(left_crossing_result, right_crossing_result):
    """
    Take the sum of the sums in the right and left crossing results. If the sum is greater than the inputs the
    left end of the subarray is the beginning in the left input and the right end is the end in the right input.
    Otherwise the result is th same as the input with the greater sum.

    Return a tuple of the beginning and the end index of the subarray, and the sum of the subarray, in that order.
    """
    crossing_sum = left_crossing_result[2] + right_crossing_result[2]
    max_sum = max(left_crossing_result[2], right_crossing_result[2], crossing_sum)

    if max_sum == crossing_sum:
        result = (left_crossing_result[0], right_crossing_result[1], max_sum)
    elif max_sum == left_crossing_result[2]:
        result = left_crossing_result
    else:
        result = right_crossing_result

    return result



if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
