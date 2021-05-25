#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author : Joey Wong
@Time : 2021/3/25 14:48
@File : 435.py
@Desc : 
"""
def func(intervals):
    intervals = sorted(intervals,key=lambda x:(x[0],x[1]))
    res = 0
    temp = []
    for interval in intervals:
        if len(temp) == 0:
            temp.append(interval)
        else:
            last = temp[-1]
            #不相交
            if interval[0] >= last[1]:
                temp.append(interval)
            else:
                if interval[1] > last[1]:
                    pass
                else:
                    temp.pop()
                    temp.append(interval)
                res += 1
    return res

if __name__ == '__main__':
    intervals = [[1,2],[2,3],[3,4],[1,3]]
    print (func(intervals))