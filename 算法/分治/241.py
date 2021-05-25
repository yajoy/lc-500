#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author : Joey Wong
@Time : 2021/3/26 14:34
@File : 241.py
@Desc : m
"""
def func(expression):
    if expression.isdigit():
        return [int(expression)]
    res = []
    for i,v in enumerate(expression):
        if v.isdigit():
            continue
        left = func(expression[:i])
        right = func(expression[i+1:])
        if v == '+':
            for l in left:
                for r in right:
                    res.append(l+r)
        elif v == '-':
            for l in left:
                for r in right:
                    res.append(l - r)
        elif v == '*':
            for l in left:
                for r in right:
                    res.append(l * r)
    return res

if __name__ == '__main__':
    expression = '1-2+3'
    print (func(expression))


