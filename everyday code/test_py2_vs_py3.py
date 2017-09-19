#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 00:19:28 2017

@author: navid
"""

from platform import python_version

import timeit

# code snippet to be executed only once
mysetup = "from math import sqrt"

# code snippet whose execution time is to be measured
mycode = '''
def example():
    i = 0
    while i < 2000000000000000000000000:
        i+=1
    return
'''

# timeit statement
print("python version is :  ",python_version())
print(timeit.timeit(setup = mysetup,
					stmt = mycode,
					number = 100000000)
    )

    
    
    
 
    
    
 