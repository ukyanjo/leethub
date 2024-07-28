class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()
        
        for idx in range(len(nums)-2):
            if idx > 0 and nums[idx] == nums[idx-1]:
                continue
                
            left, right = idx+1, len(nums)-1
            while left < right:
                sum = nums[idx] + nums[left] + nums[right]
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    output.append([nums[idx],nums[left],nums[right]])
                    
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
                    
        return output