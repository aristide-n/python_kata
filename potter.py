__author__ = 'Aristide'


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
    Algorithm description (simple greedy algorithm):
        1. Sort the list of books
        2. Create an ordered list of 5 items, each item is the count of each book in the basket, from book 1 to book 5
        5. Iterate through the list until the sum of the items is 0 (empty basket). Per iteration:
            a. add 1 to a discount ID for each book of a different type
            b. remove 1 for the count of that book
            c. the discount ID is both the count of items, and the index of the discount. At the end of the iteration,
               multiply the two and the item price (8) and add that to the total price

    """

    total = 0

    sorted(items)

    book_counts = count_same_book(items)

    discounts = [None, 1, .95, .9, .8, .75]

    discount_id = 0

    # filter 0 counts


    while sum(book_counts) > 0:

        remaining_books = filter(lambda x: x > 0, book_counts)

        print 'start'
        print remaining_books
        print book_counts

        for index, value in enumerate(book_counts):
            if len(book_counts) > 3:
                if value > 1 or discount_id == 3:
                    discount_id += 1
                    book_counts[index] -= 1

        print 'cont'
        print remaining_books
        print book_counts

        if discount_id == 0:
             for index, value in enumerate(book_counts):
                if value > 0:
                    discount_id += 1
                    book_counts[index] -= 1

        print discount_id

        total += discount_id * 8 * discounts[discount_id]
        discount_id = 0

        print 'end'
        print remaining_books
        print book_counts

    return total
