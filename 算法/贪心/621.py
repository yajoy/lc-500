#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author : Joey Wong
@Time : 2021/3/11 19:03
@File : 621.py
@Desc : m
"""
from collections import Counter

def func(tasks,n):
    dic = Counter(tasks)
    dic = sorted(dic.items(),key= lambda x:x[1],reverse=True)
    max_task_num = dic[0][1]
    temp = (n+1) * (max_task_num-1)
    for item in dic:
        if item[1] >= max_task_num:
            temp += 1

    return max(temp,len(task))





if __name__ == '__main__':
    task = ['A','A','A','B','B']
    n = 2
    print (func(task,n))
