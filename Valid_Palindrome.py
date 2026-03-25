#  Valid_Palindrome.py

class Solution:
    def isPalindrome(self,s: str) ->bool:
        cleaned = ""

        for ch in s:
            if ch.isalnum():
                cleaned+=ch.lower()

        return cleaned ==cleaned[::-1]


# Time Complexity: O(n)
# Space Complexity: O(1)
