#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author : Joey Wong
@Time : 2021/3/11 19:17
@File : 659.py
@Desc : m
"""

from collections import Counter
def func(nums):
    dic1 = Counter(nums)
    dic2 = {}
    for k in dic1.keys():
        dic2[k] = 0
    for n in nums:
        if dic1[n] == 0:
            continue
        if n-1 in dic2.keys() and dic2[n-1] > 0 :
            dic1[n] = dic1[n]-1
            dic2[n-1] = dic2[n-1]-1
            dic2[n] = dic2[n]+1
        elif n+1 in dic1.keys() and dic1[n+1] > 0 and n+2 in dic1.keys() and dic1[n+2] > 0:
            dic1[n] = dic1[n]-1
            dic1[n+1] = dic1[n+1]-1
            dic1[n+2] = dic1[n+2]-1
            dic2[n+2] = dic2[n+2]+1
        else:
            return False
    return True





if __name__ == '__main__':
    num = [1,2,3,4,5,5,6,7]
    print (func(num))
