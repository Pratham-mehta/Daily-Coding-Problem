from typing import List
class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = len(nums1), len(nums2)
        ans = 0
        
        if n2 % 2 == 1:  # If nums2 has an odd length, XOR all elements in nums1
            for num in nums1:
                ans ^= num
        
        if n1 % 2 == 1:  # If nums1 has an odd length, XOR all elements in nums2
            for num in nums2:
                ans ^= num
        
        return ans
