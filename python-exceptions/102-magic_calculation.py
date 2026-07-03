#!/usr/bin/python3


def magic_calculation(a, b):
    """Does exactly the same as the given Python bytecode."""
    result = 0

    for i in range(1, 3):
        try:
            if i > a:
                raise Exception("Too far")
            result += (a ** b) / i
        except Exception:
            result = b + a
            break

    return result
