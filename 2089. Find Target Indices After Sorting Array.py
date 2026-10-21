class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        indexList = []
        for i in range(len(nums)):
            if nums[i] == target:
                indexList.append(i)
        
        return indexList