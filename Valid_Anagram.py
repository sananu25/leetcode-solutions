# Valid_Anagram.py

class Solution:
    def isAnagram(self,s: str,t: str) -> bool:
        if len(s)!=len(t):
            return False
        count = {}
        for ch in s:
            count[ch]=count.get(ch,0) +1
        
        for ch in t:
            if ch not in count:
                return False
            count[ch]-= 1
            if count[ch] <0:
                return False
        return True


#-- Time and Space Complexity


#----Sorting Approach

#-------Time Complexity: O(n log n)
#-------Space Complexity: O(n)


#----Counting (HashMap) Approach

#-------Time Complexity: O(n)
#-------Space Complexity: O(n)


