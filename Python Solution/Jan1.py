class Solution:
    def maxScore(self, s: str) -> int:
        # Step 1: Precompute total count of ones in the string
        total_ones = s.count('1')
        
        # Step 2: Initialize variables
        max_score = 0
        left_zeros = 0
        left_ones = 0  # Number of ones in the left substring so far
        
        # Step 3: Iterate through the string (excluding the last position)
        for i in range(len(s) - 1):
            if s[i] == '0':
                left_zeros += 1
            else:
                left_ones += 1
            
            # Right ones = total ones - ones in the left substring so far
            right_ones = total_ones - left_ones
            
            # Calculate the score for the current split
            score = left_zeros + right_ones
            max_score = max(max_score, score)
        
        return max_score
