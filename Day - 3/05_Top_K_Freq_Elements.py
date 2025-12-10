###
# File: 05_Top_K_Freq_Elements.py
# Created Date: Wednesday, December 10th 2025, 10:44:23 pm
# Author: Sunny
# Last Modified: Wednesday, December 10th 2025, 11:05:07 pm
# Modified By: Sunny
###

"""
Given an integer array nums and an integer k, return the k most frequent elements within the array.

The test cases are generated such that the answer is always unique.

You may return the output in any order.

Example 1:

Input: nums = [1,2,2,3,3,3], k = 2

Output: [2,3]
Example 2:

Input: nums = [7,7], k = 1

Output: [7]
"""

from itertools import count


class Solution:
	# Using HashMap and Sorting
	def topKFrequent(self, nums: list[int], k: int) -> list[int]:
		count = {}
		for num in nums:
			count[num] = 1 + count.get(num, 0)
		
		arr = []
		for i, cnt in count.items():
			arr.append([cnt, i])
		arr.sort()

		res = []
		while len(res) < k:
			res.append(arr.pop()[1])
		return res
	
	# Using HashMap and Bucket Sort
	def topKFrequent2(self, nums: list[int], k: int) -> list[int]:
		count = {}
		freq = [[] for i in range(len(nums) + 1)]
		
		# counting the no. of times each value occurs
		for n in nums:
			count[n] = 1 + count.get(n, 0)
		# for each no.(n) and its frequency(c) in map -> append the no. to freq[c]
		for n, c in count.items():
			freq[c].append(n)
		res = []
		# loop descending, append n to res[] until length of res == k
		for i in range(len(freq) - 1, 0 , -1):
			for n in freq[i]:
				res.append(n)
				if len(res) == k:
					return res