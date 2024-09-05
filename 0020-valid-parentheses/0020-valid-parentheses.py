class Solution:
    def isValid(self, s: str) -> bool:
        tempStack = []
        matchTable = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }
        
        for char in s:
            if char not in matchTable:
                tempStack.append(char)
            elif not tempStack or matchTable[char] != tempStack.pop():
                return False
            
        return len(tempStack) == 0