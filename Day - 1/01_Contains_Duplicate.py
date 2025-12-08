###
# File: 01_Contains_Duplicate.py
# Created Date: Monday, December 8th 2025, 7:57:00 pm
# Author: Sunny
# Last Modified: Monday, December 8th 2025, 8:26:46 pm
# Modified By: Sunny
###

"""
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.
"""

from typing import List
class Solution:
	# Brute Force
	def containsDuplicate(self, nums: List[int]) -> bool:
		for i in range(len(nums)):
			for j in range(i+1,len(nums)):
				if nums[i] == nums[j]:
					return True
		return False
	
	# Using Sorting
	def containsDuplicate2(self, nums: List[int]) -> bool:
		nums.sort()
		for i in range(1, len(nums)):
			if nums[i] == nums[i-1]:
				return True
		return False

	# Using HashSet
	def containsDuplicate3(self, nums: List[int]) -> bool:
		seen = set()
		for num in nums:
			if num in seen:
				return True
			seen.add(num)
		return False
	
	# Using HashSet Length
	def containsDuplicate4(self, nums: List[int]) -> bool:
		return len(nums) != len(set(nums))