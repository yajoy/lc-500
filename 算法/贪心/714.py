#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author : Joey Wong
@Time : 2021/3/11 19:05
@File : 714.py
@Desc : m
"""
def func(prices,fee):
    dp = [[0,0] for i in range(len(prices))]
    dp[0][0] = 0
    dp[0][1] = -prices[0]
    for i in range(1,len(prices)):
        dp[i][0] = max(dp[i-1][0],dp[i-1][1] + prices[i] - fee)
        dp[i][1] = max(dp[i-1][1],dp[i-1][0]-prices[i])
    return max(dp[len(prices)-1][0],dp[len(prices)-1][1])

if __name__ == '__main__':
    prices = [1,3,2,8,4,9]
    fee = 2
    print(func(prices,fee))

