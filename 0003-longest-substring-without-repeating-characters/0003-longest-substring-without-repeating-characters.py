class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}
        start = 0
        maxLength = 0
        
        for i, char in enumerate(s):
            if char in used and start <= used[char]:
                print(i, start, used[char])
                start = used[char] + 1                
            else:
                maxLength = max(maxLength, i - start + 1)
            
            used[char] = i
        
        return maxLength
        