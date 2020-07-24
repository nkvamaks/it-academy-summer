"""Function get_ranges."""


def get_ranges(lst):
    """
    Compress list of integers into a string.

    Takes non-empty list of non-repeating integers sorted in ascending order.
    Returns string with compressed representation, e.g.
    get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) // "0-4,7-8,10"
    get_ranges([4,7,10]) // "4,7,10"
    get_ranges([2, 3, 8, 9]) // "2-3,8-9"
    """
    import itertools

    res = []
    for key, group in itertools.groupby(enumerate(lst), lambda x: x[1] - x[0]):
        group = list(group)
        res.append((group[0][1], group[-1][1]))
    return ', '.join(['{}'.format(start) if start == end else
                      '{}-{}'.format(start, end) for start, end in res])


if __name__ == '__main__':
    print(get_ranges([0, 1, 2, 3, 4, 7, 8, 10]))
    print(get_ranges([4, 7, 10]))
    print(get_ranges([2, 3, 8, 9]))
