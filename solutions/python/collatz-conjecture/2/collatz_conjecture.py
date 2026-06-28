"""Solution to the collatz conjecture exercise of exercism.org"""


def steps(number):
    """Return the number of steps required to satisfy the Collatz Conjecture.

    Args:
        number: the starting positive integer.
    Returns:
        step: the number of steps needed to reach 1.
    Raises:
        ValueError: if number is not a positive integer.
    """
    if number < 1 or not isinstance(number, int):
        raise ValueError('Only positive integers are allowed')
    step = 0
    while number > 1:
        step += 1
        is_even = number % 2 == 0
        if is_even:
            number /= 2
        else:
            number = number * 3 + 1
    return step
