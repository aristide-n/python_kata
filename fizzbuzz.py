__author__ = 'Aristide'

def fb(n):

    result = ''

    if n % 3 == 0:
        result = 'fizz'

    if n % 5 == 0:
        result += 'buzz'

    if n % 3 > 0 and n % 5 > 0:
        result = str(n)

    return result