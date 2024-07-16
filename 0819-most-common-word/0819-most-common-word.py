class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraphLower = paragraph.lower()
        paragraphTrim = re.sub(r'[^a-zA-Z]', ' ', paragraphLower)
        words = paragraphTrim.split()
        wordDict = {}
        
        for item in words:
            if item not in wordDict:
                wordDict[item] = 1
            elif item in wordDict:
                wordDict[item] +=1
        
        for bItem in banned:
            if bItem in wordDict:
                del wordDict[bItem]
        
        max_value = 0
        max_key = None
        for key,value in wordDict.items():
            if value > max_value:
                max_value = value
                max_key = key
        
        print(words)
        return(max_key)