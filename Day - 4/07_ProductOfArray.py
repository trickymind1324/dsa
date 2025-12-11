###
# File: 07_ProductOfArray.py
# Created Date: Thursday, December 11th 2025, 10:57:41 pm
# Author: Sunny
# Last Modified: Thursday, December 11th 2025, 11:02:33 pm
# Modified By: Sunny
###

"""
Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

Each product is guaranteed to fit in a 32-bit integer.

Follow-up: Could you solve it in 
O
(
n
)
O(n) time without using the division operation?

Example 1:

Input: nums = [1,2,4,6]

Output: [48,24,12,8]
Example 2:

Input: nums = [-1,0,1,2,3]

Output: [0,-6,0,0,0]
"""

class Solution:

	# Using Division
	def productExceptSelf(self, nums: list[int]) -> list[int]:
		total_product = 1
		zero_count = 0

		for num in nums:
			if num != 0:
				total_product *= num
			else:
				zero_count += 1
		
		res = []
		for num in nums:
			if zero_count > 1:
				res.append(0)
			elif zero_count == 1:
				if num == 0:
					res.append(total_product)
				else:
					res.append(0)
			else:
				res.append(total_product // num)
		
		return res

	# Using Prefix and Suffix Products Optimal
	def productExceptSelf(self, nums: list[int]) -> list[int]:
		res = [1] * len(nums)

		prefix = 1
		for i in range(len(nums)):
			res[i] = prefix
			prefix *= nums[i]

		postfix = 1
		for i in range(len(nums), -1, -1, -1):
			res[i] *= postfix
			postfix *= nums[i]
		
		return res