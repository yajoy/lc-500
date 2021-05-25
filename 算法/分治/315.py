#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author : Joey Wong
@Time : 2021/3/26 14:36
@File : 315.py
@Desc : 
"""
def func(nums):
    nums = list(enumerate(nums))
    res = [0] * len(nums)
    def merge(nums,left1,right1,left2,right2):
        l = left1
        _l = left2
        temp = []
        while left1 <= right1 and left2 <= right2:
            if nums[left1][1] <= nums[left2][1]:
                temp.append(nums[left2])
                left2 += 1
            else:
                res[nums[left1][0]] += right2 - left2 + 1
                temp.append(nums[left1])
                left1 += 1
        if left1 > right1:
            temp += nums[left2:right2+1]
        else:
            temp += nums[left1:right1+1]
        nums[l:l+len(temp)] = temp
    def merge_sort(nums,left,right):
        if left >= right:
            return
        mid = (left+right) // 2
        merge_sort(nums,left,mid)
        merge_sort(nums,mid+1,right)
        merge(nums,left,mid,mid+1,right)
    merge_sort(nums,0,len(nums)-1)
    return res

if __name__ == '__main__':
    nums = [5,2,6,1]
    print(func(nums))



