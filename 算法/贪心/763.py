#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author : Joey Wong
@Time : 2021/3/25 11:37
@File : 763.py
@Desc : 
"""
def func(S):
    res = []
    dic = {}
    for i,v in enumerate(S):
        dic[v] = i
    far = 0
    p1 = 0
    p2 = 0
    while p2 <= len(S)-1:
        temp = dic[S[p2]]
        if temp > far:
            far = temp
        if p2 == far:
            res.append(S[p1:p2+1])
            p1 = p2 + 1
        p2 += 1
    res = [len(item) for item in res]
    return res
if __name__ == '__main__':
    S = 'ababcbacadefegdehijhklij'
    print (func(S))