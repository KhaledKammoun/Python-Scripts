def new_range(x=0, y=0, z=1):
    """
    Generate a sequence of values similar to the built-in `range()` function.

    This function generates a sequence of values starting from 'x', up to 'y' (exclusive),
    with a step size of 'z'. If 'y' is not provided, the sequence starts from 0 and goes
    up to 'x' (exclusive).

    Parameters:
    x (int, optional): The starting value of the sequence. Default is 0.
    y (int, optional): The ending value of the sequence. Default is 0.
    z (int, optional): The step size between consecutive values. Default is 1.

    Returns:
    generator: A generator yielding values from the sequence.

    Raises:
    ValueError: If insufficient arguments are passed (all of 'x', 'y', and 'z' must be provided),
                or if the start value is greater than the end value.

    Example:
    >>> for c in new_range(1, 10, 2):
    ...     print(c)
    1
    3
    5
    7
    9
    """
    try:
        if not (x and y and z):
            raise ValueError("Insufficient arguments passed")
        start = 0 if y == 0 else x
        end = y if y != 0 else x
        step = z

        if start > end:
            raise ValueError("Start value cannot be greater than end value")
        while start < end:
            yield start
            start += step
    except ValueError as e:
        print("Error:", e)