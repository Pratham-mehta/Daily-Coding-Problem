class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        n = len(derived)
    
        # Helper function to check if a given starting value works
        def is_valid(start_value):
            # Initialize the original array with the first value
            original = [start_value]
            # Reconstruct the rest of the original array
            for i in range(n - 1):
                original.append(original[i] ^ derived[i])
            
            # Check if the cycle consistency holds
            return original[-1] ^ original[0] == derived[-1]

        # Check for both possible starting values (0 or 1)
        return is_valid(0) or is_valid(1)
