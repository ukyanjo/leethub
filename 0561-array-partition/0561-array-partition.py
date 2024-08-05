class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        sum = 0
        nums.sort()
        print(len(nums))
        for i in range(len(nums)//2):
            order = 2 * i
            sum += nums[order]
            
        return sum
            
            