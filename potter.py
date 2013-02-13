__author__ = 'Aristide'

"""
Potter Kata: http://craftsmanship.sv.cmu.edu/katas/potter-kata
"""

def count_same_book(items):
    counts = [0,0,0,0,0]

    counts[0] = items.count(0)
    counts[1] = items.count(1)
    counts[2] = items.count(2)
    counts[3] = items.count(3)
    counts[4] = items.count(4)

    return counts

def price(items):
    """
    The trick of the potter Kata is that there is a gap of 10% for a discount for 3 books and a discount for 4 books.
    The resulting behavior is that the discount for a set of 5 books and a set of 3 books is less than the discount
    for 2 sets of 4 books. A simple greedy algorithm does not satisfy the desired scheme.

    This is my optimal Algorithm for Potter:
    (case's solution; inspired by http://ardalis.com/a-first-pass-at-potterkata)
        1. Sort the list of books
        2. Create an ordered list of 5 items, each item is the count of each book in the basket, from book 1 to book 5
        3. Iterate through the list until the sum of the items is 0 (empty basket). Per iteration:
            I. For each book of a different type:
                a. check if there is 2 or more of that type or that we have already found exactly 3 different books
                    with the previous property
                b. add 1 to a discount ID (the discount ID is both the count of different items, and the indicator of
                    the discount.)
                c. remove 1 from the count of that type

                What the above does is that we exhaust discounts on all the possible sets of 4 before any set of 3.
                Case in point: For this set: [0, 0, the algorithm is smart to increment discount ID for item 3, but
                                              1, 1,   when it get to 4 the discount ID == 3 fails and the discount
                                              2, 2,   for 4 books is applied. The next iteration hits II.
                                              3,
                                              4]

            II. If discount ID is 0 it means that no book type accounts for more than 1 item. do b and c from I

            At the end of the iteration, multiply the count of different items (discount ID) with the discount value
            and the item price (8), and add that to the total price. If II ran in the iteration, it will be the
            end of the loop because the count of the units of each book type will be 0.
    """

    total = 0

    sorted(items)

    book_counts = count_same_book(items)

    discounts = [None, 1, .95, .9, .8, .75]

    discount_id = 0

    while sum(book_counts) > 0:

        for index, value in enumerate(book_counts):
            if value > 1 or discount_id == 3:
                discount_id += 1
                book_counts[index] -= 1

        if discount_id == 0:
             for index, value in enumerate(book_counts):
                if value > 0:
                    discount_id += 1
                    book_counts[index] -= 1

        total += discount_id * 8 * discounts[discount_id]
        discount_id = 0

    return total
