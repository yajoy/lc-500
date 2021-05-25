#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author : Joey Wong
@Time : 2021/3/11 19:17
@File : 402.py
@Desc : m
"""
def func(num,k):
    count = 0
    stack = []
    p = 0
    while  p <= len(num)-1:
        if len(stack) == 0:
            stack.append(num[p])
        else:
            while len(stack) > 0 and num[p] < stack[-1] and count < k:
                stack.pop()
                count += 1
            stack.append(num[p])
        p += 1
    if count == k:
        num = ''.join(stack)
    else:
        stack = stack[:-(k-count)]
        num = ''.join(stack)
    p = 0
    while p < len(num)-1:
        if num[p] != '0':
            break
        p += 1
    num = num[p:]
    if len(num) == 0:
        return '0'
    return num


if __name__ == '__main__':
    nums = '10200'
    k = 1
    print (func(nums,3))






