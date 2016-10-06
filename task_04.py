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
    TOTAL = 0
    for x in data:
        TOTAL = TOTAL + x
        AVERAGE = TOTAL / float(len(data))
    return TOTAL, AVERAGE
    
    
