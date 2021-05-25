#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author : Joey Wong
@Time : 2021/3/11 19:04
@File : 316.py
@Desc : m
"""
import collections

def func(s):
    stack = []
    dic = collections.Counter(s)
    for c in s:
        if c not in stack:
            while len(stack) > 0 and dic[stack[-1]] > 1 and c <= stack[-1]:
                dic[stack[-1]] -= 1
                stack.pop()
            stack.append(c)
        else:
            dic[c] -= 1
    return ''.join(stack)

if __name__ == '__main__':
    s = 'bbcaac'
    print (func(s))