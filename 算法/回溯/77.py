#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author : Joey Wong
@Time : 2021/3/26 14:45
@File : 77.py
@Desc : m
"""

res = []
def func(n,k):
    def dfs(index,k,n,path):
        global res
        if len(path) == k:
            temp =[i for i in path]
            res.append(temp)
            return
        if len(path) > k:
            return
        if len(path) + (n-index+1)< k:
            return

        for i in range(index,n+1):
            path.append(i)
            dfs(i+1,k,n,path)
            path.pop()
    dfs(1,k,n,[])

if __name__ == '__main__':
    n = 2
    k = 2
    func(n,k)
    print(res)
