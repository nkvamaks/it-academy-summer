"""Dict comprehensions."""


def dict_compr():
    """Return dict with integers 1-20 as keys and their cubes as values."""
    return {num: num**3 for num in range(1, 21)}
