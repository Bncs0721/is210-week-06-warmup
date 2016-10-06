#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Interacting with an existing list. Results can be seen in
    Resultsoftask02
"""

import data

BALLETS = data.BALLETS

del BALLETS[11]

BALLETS[1] = 'Swan Lake'

BALLETS.append('Herman Schmerman')

BALLETS.extend(['Don Quixote', 'Sylvia'])
