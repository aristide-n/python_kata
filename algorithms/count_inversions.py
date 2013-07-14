__author__ = 'Aristide'

def main():
    list_to_count = raw_input("Enter the list of numbers to count, e.g: 53784298 : ")
    print count_inversions(map(lambda char: int(char)), list(list_to_count))['count']


def count_inversions(uncounted_list):
    """
    count_inversions splits any list with more than one element in two parts, calls itself on the sublists,
    and calls count_split_inversions with the returned sorted lists. When the parameter is an empty list or a
    single element list, count_inversions just returns the list and 0 as the output.

    Doctests:
    Test empty list
        >>> count_inversions([]) == {'count': 0, 'list': []}
        True

    Test single element list
        >>> count_inversions([3]) == {'count': 0, 'list': [3]}
        True

    Test random inversions list
        >>> count_inversions([2, 4, 6, 5, 1, 3]) == {'count': 8, 'list': [1, 2, 3, 4, 5, 6]}
        True

    Test max inversions list
        >>> count_inversions([8, 7, 6, 5, 4, 3, 2, 1]) == {'count': 28, 'list': [1, 2, 3, 4, 5, 6, 7, 8]}
        True

    """
    output = {'list': [], 'count': 0}

    if len(uncounted_list) <= 1:
        output['list'] = uncounted_list
    else:
        # For odd length lists, Integer division allows a left sublist that is one element smaller than the right
        # sublist, for free :)
        left_counted = count_inversions(uncounted_list[0:(len(uncounted_list)/2)])
        right_counted = count_inversions(uncounted_list[(len(uncounted_list)/2):])

        split_counted = count_split_inversions(left_counted['list'], right_counted['list'])
        output = {'list': split_counted['list'], 'count': left_counted['count'] + right_counted['count'] + split_counted['count']}
    return output


def count_split_inversions(left_sorted_list, right_sorted_list):
    """
    count_split_inversions traverses each sorted list comparing the front elements. The smaller of the two is the
    next element in the sorted merged list. Every time the front element of the right list is lesser than the one
    of the left, it counts a number of inversions equal to the number of elements in the left list that have not been
    added to the merged list
    """
    merged_sorted_list = [None] * (len(left_sorted_list) + len(right_sorted_list))

    iLeft = 0
    iRight= 0

    iMerged = 0

    count = 0

    while iMerged < len(merged_sorted_list):
        if iLeft == len(left_sorted_list):
            merged_sorted_list[iMerged:] = right_sorted_list[iRight:]
            iMerged = len(merged_sorted_list)
        elif iRight == len(right_sorted_list):
            merged_sorted_list[iMerged:] = left_sorted_list[iLeft:]
            iMerged = len(merged_sorted_list)
        elif left_sorted_list[iLeft] < right_sorted_list[iRight]:
            merged_sorted_list[iMerged] = left_sorted_list[iLeft]
            iLeft += 1
            iMerged += 1
        else:
            merged_sorted_list[iMerged] = right_sorted_list[iRight]
            iRight +=1
            iMerged += 1
            count += (len(left_sorted_list) - iLeft)

    return {'list': merged_sorted_list, 'count': count}


if __name__ == "__main__":
    # main()
    import doctest
    doctest.testmod(verbose=True)
