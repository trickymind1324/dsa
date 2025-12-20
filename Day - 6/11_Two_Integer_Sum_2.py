###
# File: 11_Two_Integer_Sum_2.py
# Created Date: Wednesday, December 17th 2025, 11:44:54 pm
# Author: Sunny
# Last Modified: Saturday, December 20th 2025, 11:13:49 pm
# Modified By: Sunny
###

"""
Given an array of integers numbers that is sorted in non-decreasing order.

Return the indices (1-indexed) of two numbers, [index1, index2], such that they add up to a given target number target and index1 < index2. Note that index1 and index2 cannot be equal, therefore you may not use the same element twice.

There will always be exactly one valid solution.

Your solution must use 
O
(
1
)
O(1) additional space.

Example 1:

Input: numbers = [1,2,3,4], target = 3

Output: [1,2]
Explanation:
The sum of 1 and 2 is 3. Since we are assuming a 1-indexed array, index1 = 1, index2 = 2. We return [1, 2].
"""

class Solution:
	# Using Two Pointers
	def twoSum(self, numbers: list[int], target: int) -> list[int]:
		l, r = 0, len(numbers) - 1

		while(l < r):
			currSum = numbers[l] + numbers[r]
			
			if currSum > target:
				r -= 1
			elif currSum < target:
				l += 1
			else:
				return [l+1, r+1]
		
		return []
