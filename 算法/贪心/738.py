#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author : Joey Wong
@Time : 2021/3/11 19:16
@File : 738.py
@Desc : m
"""
def func(N):
    N =  [int(i) for i in str(N)]
    for i in range(len(N)-1):
        if N[i] > N[i+1]:
            index = i
            temp = N[i]-1
            while index-1 >= 0 and temp < N[index-1]:
                index -= 1
                temp = N[index] -1
            N[index] = temp
            for j in range(index+1,len(N)):
                N[j] = 9
    res = 0
    for i in N:
        res = 10 * res + i
    return res

if __name__ == '__main__':
    print (func(100))