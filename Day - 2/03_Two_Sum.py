###
# File: 03_Two_Sum.py
# Created Date: Tuesday, December 9th 2025, 9:52:22 pm
# Author: Sunny
# Last Modified: Tuesday, December 9th 2025, 10:02:55 pm
# Modified By: Sunny
###

"""
Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

Return the answer with the smaller index first.

Example 1:

Input: 
nums = [3,4,5,6], target = 7

Output: [0,1]
Explanation: nums[0] + nums[1] == 7, so we return [0, 1].

Example 2:

Input: nums = [4,5,6], target = 10

Output: [0,2]
Example 3:

Input: nums = [5,5], target = 10

Output: [0,1]
"""

from typing import List

class Solution:
	# Brute Force
	def twoSum(self, nums: List[int], target: int) -> List[int]:
		for i in range(len(nums)):
			for j in range(i + 1, len(nums)):
				if nums[i] + nums[j] == target:
					return [i,j]
		return []
	
	# Using Sorting and Two Pointers
	def twoSum2(self, nums: List[int], target: int) -> List[int]:
		temp = []

		for i, num in enumerate(nums):
			temp.append((num, i))
		
		temp.sort()
		left, right = 0, len(temp) - 1

		while left < right:
			curr = temp[left][0] + temp[right][0]
			if curr == target:
				return sorted([temp[left][1], temp[right][1]])
			elif curr < target:
				left += 1
			else:
				right -= 1
		return [] 
	
	# Using HashMap
	def twoSum3(self, nums: List[int], target: int) -> List[int]:
		res_map = {}

		for i, num in enumerate(nums):
			diff = target - num
			if diff in res_map:
				return [res_map[diff], i]
			res_map[num] = i
		return []
