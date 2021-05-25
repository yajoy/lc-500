#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author : Joey Wong
@Time : 2021/3/26 14:38
@File : 282.py
@Desc : h
"""
res = []

def func(num,target):
    def dfs(num,exp,pre,ans,target):
        if len(num) == 0:
            if ans == target:
                res.append(exp)
            return
        for i in range(len(num)):
            if i > 0 and num[0] == '0':
                continue
            left = num[:i+1]
            left_int = int(left)
            if exp == '':
                dfs(num[i+1:],left,left_int,left_int,target)
                continue
            #加
            dfs(num[i+1:],exp+'+'+left,+left_int,ans+left_int,target)

            #减
            dfs(num[i + 1:], exp+'-'+left,-left_int,ans-left_int, target)
            #乘
            dfs(num[i + 1:], exp+'*'+left, pre*left_int,ans-pre+pre*left_int,target)
    dfs(num,'',0,0,target)







if __name__ == '__main__':
    num = '00'
    target = 0
    func(num,target)
    print (res)