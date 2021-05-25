#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author : Joey Wong
@Time : 2021/3/26 14:45
@File : 131.py
@Desc : m
"""
res = []
def func(s):
    def check(s):
        l = 0
        r = len(s) - 1
        while l <= r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
    def dfs(index,s,path):
        if index == len(s) and len(path) > 0:
            temp =  [i for i in path]
            res.append(temp)
        for i in range(index,len(s)):
            if check(s[index:i+1]):
                path.append(s[index:i+1])
                dfs(i+1,s,path)
                path.pop()

    dfs(0,s,[])

if __name__ == '__main__':
    s = 'a'
    func(s)
    print(res)