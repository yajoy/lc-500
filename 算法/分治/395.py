#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author : Joey Wong
@Time : 2021/3/26 14:35
@File : 395.py
@Desc : m
"""
from collections import Counter
def func(s,k):
    def dfs(s,k):
        if not s:
            return 0
        c = Counter(s)
        res = 0
        for i,v in enumerate(s):
            if c[v] < k:
                left = dfs(s[:i],k)
                right = dfs(s[i+1:],k)
                return max(left,right)
            else:
                res += 1
        return res
    return dfs(s,k)

if __name__ == '__main__':
    print (func('bbaaacb',3))