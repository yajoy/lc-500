#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author : Joey Wong
@Time : 2021/3/11 10:31
@File : 605.py
@Desc : e
"""
def func(flowerbed,k):
    l = len(flowerbed)
    for i in range(l):
        if flowerbed[i] == 0:
            if i-1 >= 0 and i+1 <= l-1:
                if flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                    flowerbed[i] = 1
                    k -= 1
            elif i-1 <= 0 and i+1 <= l-1:
                if flowerbed[i+1] == 0:
                    flowerbed[i] = 1
                    k -= 1
            elif i-1 >= 0 and i+1 > l-1:
                if flowerbed[i-1] == 0:
                    flowerbed[i] = 1
                    k -= 1
            else:
                flowerbed[i] = 1
                k -= 1
    if k <= 0:
        return True
    else:
        return False

if __name__ == '__main__':
    flowerbed = [1,0,0,0,1]
    n = 2
    print (func(flowerbed,n))





