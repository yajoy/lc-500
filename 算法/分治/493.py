#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author : Joey Wong
@Time : 2021/3/26 14:36
@File : 493.py
@Desc : h
"""

count = 0
def func(nums):

    def merge(nums,l1,r1,l2,r2):
        global count
        temp = []
        i = l1
        j = l2
        l = l1



        while l1 <= r1 and l2 <= r2:
            if nums[l1] < nums[l2]:
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
    merge_sort(nums,0,len(nums)-1)
    return count

if __name__ == '__main__':
    nums = [1,3,2,3,1]
    print (func(nums))
    print (nums)