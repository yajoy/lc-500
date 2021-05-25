#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author : Joey Wong
@Time : 2021/3/26 14:46
@File : 51.py
@Desc : h
"""
res = []
def func(n):
    def check(i,j,n):
        #检查列
        for k in range(i):
            if board[k][j] == 'Q':
                return False
        #检查主对角线
        _i = i-1
        _j = j-1
        while _i >= 0 and _j >= 0:
            if board[_i][_j] == 'Q':
                return False
            _i -= 1
            _j -= 1
        #检查辅对角线
        _i = i-1
        _j = j+1
        while _i >= 0 and _j+1 <= n:
            if board[_i][_j] == 'Q':
                return False
            _i -= 1
            _j += 1
        return True
    def dfs(i,board,n):
        global res
        if i == n:
            temp = [''.join(i) for i in board]
            res.append(temp)
            return
        for j in range(n):
            if check(i,j,n):
                board[i][j] = 'Q'
                dfs(i+1,board,n)
                board[i][j] = '.'

    board = [['.'] * n for i in range(n)]
    dfs(0,board,n)
if __name__ == '__main__':
    n = 4
    func(n)
    print(res)





