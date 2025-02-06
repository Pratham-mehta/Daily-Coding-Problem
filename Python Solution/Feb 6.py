# Distinct Postive Integers : nums
# Output : return number of tuples (a,b,c,d) -> integer value
# Condition : Output should be in a*b = c*d and a!=b!=c!=d
from collections import defaultdict # for using count
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        p_count = defaultdict(int)
        n = len(nums)

        # step 1 : Count the frequency of each product a*b
        for i in range(n):
            for j in range(i+1,n):
                p = nums[i]*nums[j]
                p_count[p] += 1
        
        # step 2 : Calculate the total number of valid tuples
        total = 0
        for c in p_count.values():
            if c>=2:
                total += c * (c-1)*4
        
        return total
