#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author : Joey Wong
@Time : 2021/3/26 14:46
@File : 10.py
@Desc : h
"""

def func(s,p):
    def match(i,j):
        if i == 0:
            return False
        if p[j-1] == '.':
            return True
        return s[i-1] == p[j-1]
    dp = []
    for i in range(len(s) + 1):
        dp.append([False]*(len(p)+1))
    dp[0][0] = True
    for i in range(len(s)+1):
        for j in range(1,len(p)+1):
            if p[j-1] == '*':
                dp[i][j] = dp[i][j-2]
                if match(i,j-1):
                    dp[i][j] |= dp[i-1][j]
            else:
                if match(i,j):
                    dp[i][j] = dp[i-1][j-1]

    return dp[-1][-1]
if __name__ == '__main__':
    s = ''
    p = '.'
    res = func(s,p)
    print(res)