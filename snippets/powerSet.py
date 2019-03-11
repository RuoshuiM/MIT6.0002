# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 08:20:43 2019

@author: ruosh
"""
from itertools import combinations, chain
def powerSet(items):
    return chain.from_iterable(combinations(items, s) for s in range(len(items) + 1))
