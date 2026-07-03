#!/usr/bin/python3
"""Module that divides two lists element by element."""


def list_division(my_list_1, my_list_2, list_length):
    """Divide elements of two lists, handling errors.

    Args:
        my_list_1 (list): The first list (dividends).
        my_list_2 (list): The second list (divisors).
        list_length (int): The length of the result list.

    Returns:
        list: A list of division results, with 0 on error.
    """
    new_list = []
    for i in range(list_length):
        result = 0
        try:
            result = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            new_list.append(result)
    return new_list
