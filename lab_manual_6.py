def square_number(n):
    """Return the square of a number."""
    if not isinstance(n, (int, float)):
        raise TypeError("Input must be a number")
    return n * n
print(square_number(8))