from typing import List


def sum_of_numbers(numbers: List[int]) -> int:
    """ Adding all numbers from the list.
    
    :returns: Sum of all the numbers.
    :rtype: int
    """

    try:
        total = sum(numbers)
    except ValueError as ve:
        raise ValueError(f"Oops! List contains values which are not integers: {ve}")
    except TypeError as te:
        raise TypeError(f"TypeError occurred which prevented calculating the sum: {te}")
    except Exception as e:
        raise Exception(f"Exception occurred which prevented calculating the sum: {e}")

    return total
