"""
Given an unsorted integer array nums, return the smallest missing positive integer.
You must implement an algorithm that runs in O(n) time and uses constant extra space.
Example 1:
Input: nums = [1,2,0]
Output: 3
----------
Example 2:
Input: nums = [3,4,-1,1]
Output: 2
----------
Example 3:
Input: nums = [7,8,9,11,12]
Output: 1
Nice explanation: https://www.enjoyalgorithms.com/blog/first-missing-positive
"""
from typing import List

def firstMissingPositiveElegantSolution(nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = 1000000000
            print(f"{i} - {nums[i]}")
            print("-----")
        print("*********")
        for i in range(n):
            if abs(nums[i]) != 1000000000:

                nums[abs(nums[i])-1] = -abs(nums[abs(nums[i])-1])
            print(f"{i} - {nums[i]}")
            print("-----")
        print("*********")
        for i in range(n):
            if nums[i] > 0:
                return i+1
            print(f"{i} - {nums[i]}")
            print("-----")
        return n+1

def firstMissingPositive(nums: [int]) -> int:
    """This solution takes O(2n) in time and O(1) in space"""
    d = {int:bool}
    for num in nums:
      d[num] = None

    for i in range(1, len(nums)+1, 1):
      if i not in d:
        return i
    return len(nums)+1

if __name__ == "__main__":
    l = [3,4,-1,1]
    print(firstMissingPositive(l))


