#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Using the for loop"""


def process_data(data):
    """Provides the total sum and average of the values passed.

    Args:
        data ([list]) or((tuple)): values to be operated on.

    Returns:
        TOTAL = sum of values added to [list]  or (tuple).
        AVERAGE = average of values added to [list] or (tuple).

    Examples:

        >>> process_data((1, 2, 3))
            (6, 2.0)

        >>> process_data([22, 18, 21, 16])
            (77, 19.25)

    """
    total_sum = 0
    for variable in data:
        total_sum = total_sum + variable
        average_data = total_sum / float(len(data))
    return total_sum, average_data
