__author__ = 'Aristide'


def fizzbuzz(n):
    """
    My first time trying python's doctest: http://docs.python.org/2/library/doctest.html

    A program that prints the numbers from 1 to 100. But for multiples of three print "Fizz" instead of the number
    and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print
    "FizzBuzz?".
    More:
    A number is Fizz if it is divisible by 3 or if it has a 3 in it
    A number is Buzz if it is divisible by 5 or if it has a 5 in it
    A number is FizzBuzz if it is divisible by 5 and 3 or if it has a 5 and a 3 in it

    >>> [fizzbuzz(n) for n in range(1,16)]
    [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 'Fizz', 14, 'FizzBuzz']

    >>> fizzbuzz(151)
    'Buzz'

    >>> fizzbuzz(253)
    'FizzBuzz'
    """
    if 0 == n % 15 :
        return "FizzBuzz"
    elif 0 == n % 3 :
        return "Fizz"
    elif 0 == n % 5 :
        return "Buzz"
    elif all (c in str(n) for c in '53'):
        return 'FizzBuzz'
    elif any (c is '3' for c in str(n)):    #Same as: elif str(n).find('3') is not -1:
        return 'Fizz'
    elif any (c is '5' for c in str(n)):
        return 'Buzz'

    return n


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)