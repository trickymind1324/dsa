###
# File: 04_Group_Anagrams.py
# Created Date: Tuesday, December 9th 2025, 10:36:22 pm
# Author: Sunny
# Last Modified: Tuesday, December 9th 2025, 11:11:39 pm
# Modified By: Sunny
###

"""
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: strs = ["act","pots","tops","cat","stop","hat"]

Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
Example 2:

Input: strs = ["x"]

Output: [["x"]]
Example 3:

Input: strs = [""]

Output: [[""]]
"""

from collections import defaultdict


class Solution:
	# Using Sorting
	def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
		res = defaultdict(list)
		for s in strs:
			sorted_str = ''.join(sorted(s))
			res[sorted_str].append(s)
		return list(res.values())
	
	# Using Hash Table
	def groupAnagrams2(self, strs: list[str]) -> list[list[str]]:
		res = defaultdict(list)

		for s in strs:
			count = [0] * 26 # as there are 26 letters in the English alphabet

			for char in s:
				count[ord(char) - ord('a')] += 1
			
			res[tuple(count)].append(s)
		
		return list(res.values())