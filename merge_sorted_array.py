#merge_sorted_array.py

class Solution:
    def merge(self,nums1,m,nums2, n):
        for i in range(n):
            nums1[m+ i] =nums2[i]
    
        nums1.sort()

#Complexity
#Time:O((m+n) log(m+n))
#Space:O(1)
