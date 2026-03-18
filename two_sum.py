two_sum.py
# Problem: Two Sum
# Platform: LeetCode
# Approach: HashMap (Dictionary)
# Time Complexity: O(n)
# Space Complexity: O(n)


class Solution:
    def twoSum(self, nums, target):
        mp = {}
        
        for i in range(len(nums)):
            complement = target - nums[i]
            
            if complement in mp:
                return [mp[complement], i]
            
            mp[nums[i]] = i
        
        return []
