from itertools import chain, islice, repeat

# TODO need docs!


def chunk(it, size):
    """
    https://stackoverflow.com/a/22045226
    """
    it = iter(it)
    return iter(lambda: tuple(islice(it, size)), ())


def chunk_pad(it, size, padval=None):
    """
    https://stackoverflow.com/a/22045226
    """
    it = chain(iter(it), repeat(padval))
    return iter(lambda: tuple(islice(it, size)), (padval,) * size)


def chunks(l, n):
    """
    https://stackoverflow.com/a/1751478
    """
    n = max(1, n)
    return (l[i : i + n] for i in range(0, len(l), n))
