class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        # Initialize the length first
        n = len(s)
        # Intialize the shift array
        shift_array = [0] * (n+1)

        # Now process each shift operation
        for start, end, direction in shifts:
            if direction==1:
                shift_array[start] +=1 # if direction is forward, then increment the range
                shift_array[end + 1] -= 1
            else:
               shift_array[start] -=1 
               shift_array[end+1] +=1

        cumulative_shift = 0
        for i in range(n):
            cumulative_shift += shift_array[i]
            shift_array[i] = cumulative_shift
        
        res = []
        for i in range(n):
            original_char = s[i]
            shift = shift_array[i]
            new_char = chr((ord(original_char)-ord('a')+shift)%26+ord('a'))
            res.append(new_char)

        return ''.join(res)
