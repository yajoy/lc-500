#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author : Joey Wong
@Time : 2021/3/26 14:45
@File : 93.py
@Desc : m
"""
res = []
def func(s):
    def dfs(s,index,path):
        if len(path) >= 4:
            if len(path) == 4 and index == len(s):
                res.append('.'.join(path))
            return
        for i in range(index,index+3):
            if i >= len(s):
                break
            if i > index and s[index] == '0':
                break
            if int(s[index:i+1]) > 255:
                break
            path.append(s[index:i+1])
            dfs(s,i+1,path)
            path.pop()
    dfs(s,0,[])





if __name__ == '__main__':
    s = '25525511135'
    func(s)
    print(res)