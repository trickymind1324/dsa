###
# File: 06_Encode_Decode_String.py
# Created Date: Thursday, December 11th 2025, 9:12:30 pm
# Author: Sunny
# Last Modified: Thursday, December 11th 2025, 9:29:56 pm
# Modified By: Sunny
###

"""
Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

Please implement encode and decode

Example 1:

Input: ["neet","code","love","you"]

Output:["neet","code","love","you"]
Example 2:

Input: ["we","say",":","yes"]

Output: ["we","say",":","yes"]
"""

class Solution:
	# Encoding and Decoding using Length Prefixing
	def encode(self, strs: list[str]) -> str:
		if not strs:
			return ""
		
		sizes, res = [], ""

		for s in strs:
			sizes.append((len(s)))

		for t in sizes:
			res += str(t)
			res += ','
		res += '#'

		for s in strs:
			res += s
		return res
		
	def decode(self, s: str) -> list[str]:
		if not s:
			return []
		
		sizes, res, i = [], [], 0

		while s[i] != '#':
			cur = ""
			while s[i] != ',':
				cur += s[i]
				i += 1
			sizes.append(int(cur))
			i += 1
		i += 1 # skip the '#'

		for t in sizes:
			res.append(s[i:i + t])
			i += t
		return res