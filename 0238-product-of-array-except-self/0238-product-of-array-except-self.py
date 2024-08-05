class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        multList = []
        seed  = 1
        
        for i in range(len(nums)):
            multList.append(seed)
            seed *= nums[i]
        
        seed2 = 1
        for i in range(len(nums)-1,-1,-1):
            multList[i] = multList[i] * seed2
            seed2 *= nums[i]
            
        return multList