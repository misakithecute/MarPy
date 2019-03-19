def bubble_sort(items):
    '''
    Returns an array of items, sorted in ascending order

    Parameters
    -----------
    items: list
        A list of unordered numbers

    Returns
    --------
    list
        list of elements in items, sorted in ascending order.
    '''
    moo1 = len(items) - 1

    for x in range(len(items)):
        for y in range(moo1 - x):
            if items[y] > items[y+1]:
                items[y], items[y+1] = items[y+1], items[y]

    return items



def merge(i1,i2):
    """
    Merges two sorted lists of numbers

    Parameters
    -----------
    i1 : list
        A sorted list of numbers
    i2 : list
        A sorted list of numbers

    Returns
    --------
    list
        a single list of sorted numbers.
    """

    results = []

    while len(i1) > 0 and len(i2) > 0:
        if i1[0] < i2[0]:
            results.append(i1[0])
            i1.pop(0)
        else:
            results.append(i2[0])
            i2.pop(0)

    if len(i1) == 0:
        results = results + i2
    if len (i2) == 0:
        results = results + i1

    return results

def merge_sort(items):
        '''
        Returns an array of items, sorted in ascending order.

        Parameters
        -----------
        items: list
            A list of unordered numbers

        Returns
        --------
        list
            list of elements in items, sorted in ascending order.
        '''
        if len(items) <= 1:
            return items
        mid = len(items) // 2
        i1 = items[:mid]
        i2 = items[mid:]

        i1 = merge_sort(i1)
        i2 = merge_sort(i2)

        return list(merge(i1,i2))


def quick_sort(items):
    '''
    Returns an array of items, sorted in ascending order

    Parameters
    -----------
    items: list
        A list of unordered numbers

    Returns
    --------
    list
        list of elements in items, sorted in ascending order.
    '''

    l = []
    p = []
    m = []

    if len(items) <= 1:
        return items
    else:
        pivot = items[0]
        for x in items:
            if x < pivot:
                l.append(x)
            elif x > pivot:
                m.append(x)
            else:
                p.append(x)

        l = quick_sort(l)
        m = quick_sort(m)
        return l + p + m
