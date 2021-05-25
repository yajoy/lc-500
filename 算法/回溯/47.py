#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author : Joey Wong
@Time : 2021/3/26 14:46
@File : 47.py
@Desc : m
"""
res = []
def func(nums):
    def dfs(nums,flag,path):
        global res
        if len(path) == len(nums):
            temp  =  [i for i in path]
            res.append(temp)
            return
        for i,v in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1] and flag[i-1] != False:
                continue
            if flag[i] != True:
                flag[i] = True
                path.append(v)
                dfs(nums,flag,path)
                path.pop()
                flag[i] = False
    flag = [False] * len(nums)
    nums = sorted(nums)
    dfs(nums,flag,[])

if __name__ == '__main__':
    nums = [1,1,2]
    func(nums)
    print(res)




