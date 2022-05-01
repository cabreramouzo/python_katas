"""
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
There is only one repeated number in nums, return this repeated number.
You must solve the problem without modifying the array nums and uses only constant extra space.
https://leetcode.com/problems/find-the-duplicate-number/submissions/

Example 1:

Input: nums = [1,3,4,2,2]
Output: 2
Example 2:

Input: nums = [3,1,3,4,2]
Output: 3
"""

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        d = {int: bool}
        
        for num in nums:
            if num in d:
                return num
            d[num] = True


