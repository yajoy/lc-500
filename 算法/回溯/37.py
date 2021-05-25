#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author : Joey Wong
@Time : 2021/3/26 14:47
@File : 37.py
@Desc : h
"""

def func(borad):
    dic = {}
    def dfs(i,j,borad,_board):
        if j >= 9:
            i += 1
            j = 0
        if i >= 9:
            return
        while j < 9 and borad[i][j] != '.':
            j += 1
        ii = i % 3
        jj = j % 3
        temp = _board[ii][jj]
        for k,v in temp.items():
            if v == 0:
                if and
                    dfs(i,j+1,borad,_board)




