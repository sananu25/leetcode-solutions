two_sum.py
# Problem: Two Sum
# Platform: LeetCode
# Approach: HashMap (Dictionary)
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap={}

        for i,n in enumerate(nums):
            diff=target-n
            if diff in prevMap:
                return[prevMap[diff],i]
            prevMap[n]=i
