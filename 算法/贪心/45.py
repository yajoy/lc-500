#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author : Joey Wong
@Time : 2021/3/11 19:01
@File : 45.py
@Desc : m
"""

def func(nums):
    i = 0
    l = len(nums)
    res = 0
    while i <= l-1:
        if i == l-1:
            return res
        temp = 0
        temp_index = 0
        for j in range(1,nums[i]+1):
            if i+j < l-1:
                if i+j+nums[i+j] > temp:
                    temp = i+j+nums[i+j]
                    temp_index = i+j
            if i+j == l-1:
                return res + 1
        i = temp_index
        res += 1








if __name__ == '__main__':
    nums = [3,2,1]
    print(func(nums))