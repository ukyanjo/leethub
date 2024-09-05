class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        waitDays = [0] * len(temperatures)
        stack = []
        for i, cur in enumerate(temperatures):
            while stack and cur > temperatures[stack[-1]]:
                last = stack.pop()
                waitDays[last] = i-last
                
            stack.append(i)
        
        return waitDays