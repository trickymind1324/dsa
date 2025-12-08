###
# File: 02_Valid_Anagram.py
# Created Date: Monday, December 8th 2025, 8:51:10 pm
# Author: Sunny
# Last Modified: Monday, December 8th 2025, 9:20:48 pm
# Modified By: Sunny
###

"""
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
"""

class Solution:
	# Using Sorting
	def isAnagram(self, s: str, t: str) -> bool:
		return sorted(s) == sorted(t)
	
	# Using HashMap
	def isAnagram2(self, s: str, t: str) -> bool:
		if len(s) != len(t):
			return False
		
		countS, countT = {}, {}

		for i in range(len(s)):
			countS[s[i]] = 1 + countS.get(s[i], 0)
			countT[t[i]] = 1 + countT.get(t[i], 0)

		return countS == countT
	
	# Using Hash Table
	def isAnagram3(self, s: str, t: str) -> bool:
		if len(s) != len(t):
			return False
		
		count = [0] * 26 # as there are 26 letters in the English alphabet

		for i in range(len(s)):
			count[ord(s[i]) - ord('a')] += 1
			count[ord(t[i]) - ord('a')] -= 1

		for val in count:
			if val != 0:
				return False
		return True