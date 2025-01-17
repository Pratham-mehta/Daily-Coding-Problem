class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        # Helper function to check if a character is a vowel
        def is_vowel(char):
            return char in {'a', 'e', 'i', 'o', 'u'}
        
        # Precompute whether each word starts and ends with a vowel
        is_vowel_word = [
            is_vowel(word[0]) and is_vowel(word[-1]) for word in words
        ]
        
        # Create prefix sum array
        n = len(words)
        prefix = [0] * n
        prefix[0] = 1 if is_vowel_word[0] else 0
        for i in range(1, n):
            prefix[i] = prefix[i - 1] + (1 if is_vowel_word[i] else 0)
        
        # Answer the queries
        result = []
        for li, ri in queries:
            if li == 0:
                result.append(prefix[ri])
            else:
                result.append(prefix[ri] - prefix[li - 1])
        
        return result
