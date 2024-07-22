class Solution:
    def longestPalindrome(self, s: str) -> str:
        tempDict = defaultdict(list)
        for num in range(1, len(s)+1):
            for idx in range(len(s)-(num-1)):
                if(s[idx:idx+num] == s[idx:idx+num][::-1]):
                    tempDict[num].append(s[idx:idx+num])    
                    
        return tempDict[list(tempDict.keys())[-1]][0]