###
# File: 14_Binary_Search.py
# Created Date: Sunday, December 21st 2025, 6:21:52 pm
# Author: Sunny
# Last Modified: Sunday, December 21st 2025, 6:48:35 pm
# Modified By: Sunny
###

"""
You are given an array of distinct integers nums, sorted in ascending order, and an integer target.

Implement a function to search for target within nums. If it exists, then return its index, otherwise, return -1.

Your solution must run in O(logn) time.

Example 1:

Input: nums = [-1,0,2,4,6,8], target = 4

Output: 3
Example 2:

Input: nums = [-1,0,2,4,6,8], target = 3

Output: -1
"""

class Solution:
    def search(self, nums: list[int], target: int):
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + ((r - l) // 2)
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                return mid
        return -1