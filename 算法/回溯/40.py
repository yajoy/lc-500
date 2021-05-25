#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author : Joey Wong
@Time : 2021/3/26 14:45
@File : 40.py
@Desc : m
"""
res = []
def func(candidates,target):
    def dfs(candidates,index,path,target):
        global res
        if sum(path) == target:
            temp = [i for i in path]
            res.append(temp)
            return
        if sum(path) > target:
            return
        if index == len(candidates):
            return
        for i in range(index,len(candidates)):
            if i > index and candidates[i] == candidates[i-1] :
                continue
            path.append(candidates[i])
            dfs(candidates,i+1,path,target)
            path.pop()
    candidates = sorted(candidates)
    dfs(candidates,0,[],target)
    return res




if __name__ == '__main__':
    candidates = [2,5,2,1,2]
    target = 3
    func(candidates,target)
    print(res)

