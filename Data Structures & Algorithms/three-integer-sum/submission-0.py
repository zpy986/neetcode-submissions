class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        for i in range(len(nums)):
            seen = {}
            for j in range(i + 1,len(nums)):
                target = -nums[i] - nums[j]
                if target in seen:
                    res.add(tuple(sorted([target, nums[i], nums[j]])))
                if nums[j] not in seen:
                    seen[nums[j]] = j
                
        
        return [list(x) for x in res]
                