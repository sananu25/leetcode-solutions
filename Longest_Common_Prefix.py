# Longest_Common_Prefix.py


from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""      
        for i in range(len(strs[0])):
            for s in strs:
                if i >=len(s) or s[i]!=strs[0][i]:
                    return res
            res+=strs[0][i]        
        return res


#Time Complexity:O(n * m)
#Space Complexity: O(1)
