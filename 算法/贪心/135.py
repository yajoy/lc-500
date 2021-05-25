#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author : Joey Wong
@Time : 2021/3/11 19:18
@File : 135.py
@Desc : h
"""
def func(nums):
    temp = [1] * len(nums)
    for i in range(1,len(nums)):
        if nums[i] > nums[i-1]:
            temp[i] = temp[i-1]+1
    for j in range(len(nums)-2,-1,-1):
        if nums[j] > nums[j+1]:
            temp[j] = max(temp[j+1]+1,temp[j])
    return sum(temp)

def viterbi(x,trans):
    path = []
    dp = [0.0] * len(trans)
    for i in range(len(trans)):
        path.append([i])
    for i in range(len(x)):
        if i == 0:
            dp = x[i]
            continue
        cur = x[i]
        for j in range(len(trans)):
            min_p = 0
            k_temp = -1
            for k in range(len(trans)):
                 p = dp[k] * trans[k][j] * cur[j]
                 if p > min_p:
                     min_p = p
                     k_temp = k
            path[j] = path[k_temp] + [j]
            dp[j] = min_p
    min_p = 0
    path_index = 0
    for i,v in enumerate(dp):
        if v > min_p:
            min_p = v
            path_index = i
    return path[path_index]






if __name__ == '__main__':
    x = [
        [0.5,0.3,0.2],
        [0.1,0.4,0.5],
        [0.7,0.2,0.1]
    ]
    trans = [
        [0.4,0.1,0.5],
        [0.2,0.7,0.1],
        [0.3,0.2,0.6],
    ]
    print (viterbi(x,trans))