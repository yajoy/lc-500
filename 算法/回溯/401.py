#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author : Joey Wong
@Time : 2021/3/26 14:39
@File : 401.py
@Desc : e
"""
res = []
def fun(n):
    hours = [8,4,2,1,0,0,0,0,0,0]
    minites = [0,0,0,0,32,16,8,4,2,1]
    def dfs(n,hours,minites,hour,minite,index):
        if hour > 11 or minite > 59:
            return
        if n <= 0:
            temp = ''
            if minite >=0 and minite <= 9:
                temp = str(hour) +':' + '0' + str(minite)
            else:
                temp = str(hour) + ':' +str(minite)
            res.append(temp)
            return
        for i in range(index,10):
            dfs(n-1,hours,minites,hour+hours[i],minite+minites[i],i+1)
    dfs(n,hours,minites,0,0,0)

if __name__ == '__main__':
    fun(6)
    print(res)
