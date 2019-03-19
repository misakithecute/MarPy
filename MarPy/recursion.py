def sum_array(array):
    '''
    Returns the sum of all elements in array

    Parameters
    ----------
    array: list
        list of unsorted numbers(int or float)

    Returns
    -------
    int or float
        the sum of all elements in array.
    '''

    if len(array) == 0:
        return 0
    else:
        return array[0] + sum_array(array[1:])


def fibonacci(n):
    '''
    Returns the nth term in fibonacci sequence

    Parameters
    ----------
    n: int
        the nth term in fibonacci sequence to calculate

    Returns
    -------
    int
        the nth term of the fibonacci sequence,
        equal to sum of previous two terms.
    '''
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n -2)


def factorial(n):
    '''
    Returns n!

    Parameters
    ----------
    n: int
        the number to apply to the factorial

    Returns
    -------
    int
        the factorial of n.
    '''
    if n == 1:
        return n
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)


def reverse(word):
    '''
    Returns word in reverse

    Parameters
    ----------
    word: string
        a word to be reversed

    Returns
    -------
    string
        the word in reversed order starting with last letter and
        ending with first letter.
    '''
    if len(word) == 0:
        return word
    else:
        return reverse(word[1:]) + word[0]
