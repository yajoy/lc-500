#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author : Joey Wong
@Time : 2021/3/26 14:36
@File : 327.py
@Desc : h
"""
res = 0
def func(nums,lower,upper):
    nums = [0] + nums
    pre_sum = [0] * len(nums)
    for i in range(1,len(nums)):
        pre_sum[i] = pre_sum[i-1] + nums[i]
    def merge(nums,l1,r1,l2,r2):
        global res
        temp = []
        l = l1
        i = l1
        j = l2
        k = l2
        while i <=  r1:
            while j <= r2 and nums[j] - nums[i] <= upper:
                j += 1
            while k <= r2 and nums[k] - nums[i] < lower:
                k += 1
            res += j - 1  - k + 1
            i += 1

        while l1 <= r1 and l2 <= r2:
            if nums[l1] <= nums[l2]:
                temp.append(nums[l1])
                l1 += 1
            else:
                temp.append(nums[l2])
                l2 += 1
        if l1 > r1:
            temp += nums[l2:r2+1]
        else:
            temp += nums[l1:r1+1]
        nums[l:l+len(temp)] = temp
    def merge_sort(nums,left,right):
        if left >= right:
            return
        mid = (left+right) // 2
        merge_sort(nums,left,mid)
        merge_sort(nums,mid+1,right)
        merge(nums,left,mid,mid+1,right)
    merge_sort(pre_sum,0,len(pre_sum)-1)




if __name__ == '__main__':
    nums = [-2,5,-1]
    lower = -2
    upper = 2
    func(nums,lower,upper)