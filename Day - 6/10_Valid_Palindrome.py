###
# File: 10_Valid_Palindrome.py
# Created Date: Wednesday, December 17th 2025, 11:38:24 pm
# Author: Sunny
# Last Modified: Saturday, December 20th 2025, 10:55:08 pm
# Modified By: Sunny
###

"""
Given a string s, return true if it is a palindrome, otherwise return false.

A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).

Example 1:

Input: s = "Was it a car or a cat I saw?"

Output: true
Explanation: After considering only alphanumerical characters we have "wasitacaroracatisaw", which is a palindrome.

Example 2:

Input: s = "tab a cat"

Output: false
Explanation: "tabacat" is not a palindrome.
"""

class Solution:
	# Using Two Pointers
	def isPalindrome(self, s: str):
		l, r = 0, len(s) - 1

		while l < r:
			while l < r and not self.isAlphaNum(s[l].lower()):
				l += 1
			while r > l and not self.isAlphaNum(s[r].lower()):
				r -= 1
			
			if s[l].lower() != s[r].lower():
				return False
			l += 1
			r -= 1
		return True


	def isAlphaNum(self, c: str):
		return (c >= 'a' and c <= 'z') or (c >= '0' and c <= '9')