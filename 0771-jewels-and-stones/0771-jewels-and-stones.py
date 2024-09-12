class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        tempMap = {}
        for char in stones:
            if char in tempMap:
                tempMap[char] += 1
            else:
                tempMap[char] = 1
        
        print(tempMap)
        count = 0
        for char in jewels:
            if char in tempMap:
                count += tempMap[char]

        return count