#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Testing the mutability differences between strings and tuples"""


def flip_keys(to_flip):
    """Provides the values of the items entered in reversed.

    Args:
    to_flip [list] or (tuple): values to be reversed.

    Returns:
    Original list with values reversed.

    Examples:

        >>>flip_keys([(1, 2, 3), 'abc'])
           [(3, 2, 1), 'cba']

        >>>flip_keys([(6, 3, 7), 'zcb'])
           [(7, 3, 6), 'bcz']
    """
    counter = 0
    for variable in to_flip:
        to_flip[counter] = variable[::-1]
        counter += 1
        if counter == len(to_flip):
            return to_flip
