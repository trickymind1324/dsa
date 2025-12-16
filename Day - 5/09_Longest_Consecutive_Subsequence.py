###
# File: 09_Longest_Consecutive_Subsequence.py
# Created Date: Tuesday, December 16th 2025, 11:35:03 pm
# Author: Sunny
# Last Modified: Tuesday, December 16th 2025, 11:37:34 pm
# Modified By: Sunny
###

"""
Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.

A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. The elements do not have to be consecutive in the original array.

You must write an algorithm that runs in O(n) time.

Example 1:

Input: nums = [2,20,4,10,3,4,5]

Output: 4
Explanation: The longest consecutive sequence is [2, 3, 4, 5].

Example 2:

Input: nums = [0,3,2,5,4,6,1,1]

Output: 7
"""
from typing import List

class Solution:
    # Using HashSet
    def longestConsecutive(self, nums: List[int]) -> int:
        mySet = set(nums)
        longSeq = 0

        for n in nums:
            # Check if it's the start of a sequence
            if (n - 1) not in mySet:
                currSeq = 0
                while (n + currSeq) in mySet:
                    currSeq += 1
                longSeq = max(currSeq, longSeq)
        return longSeq