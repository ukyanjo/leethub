class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedStrs = []
        for str in strs:
            sortedStrs.append(''.join(sorted(str)))
        
        trimmedStrs = list(set(sortedStrs))
        tempReturnList = [[str] for str in trimmedStrs]
        tempIdxList = [[] for idx in range(len(trimmedStrs))]
        returnList = [[] for idx in range(len(trimmedStrs))]
        
        tupledStrs = [(idx, str) for idx, str in enumerate(sortedStrs)]
        for tupledStr in tupledStrs:
            idxT, sortedStr = tupledStr
            for idxL,tempList in enumerate(tempReturnList):
                if sortedStr == tempList[0]:
                    tempIdxList[idxL].append(idxT)
                    
        for idxL, idxList in enumerate(tempIdxList):
            for idx in idxList:
                returnList[idxL].append(strs[idx])
                
        return returnList