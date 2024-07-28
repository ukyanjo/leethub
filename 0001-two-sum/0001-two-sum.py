class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx, num in enumerate(nums):
            pivot = nums[idx]
            for idx2, num2 in enumerate(nums):
                if idx == idx2:
                    continue
                if pivot + num2 == target:
                    return [idx,idx2]
            