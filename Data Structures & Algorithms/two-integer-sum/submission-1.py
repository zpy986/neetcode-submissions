class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        res = []

        for i in range(len(nums)):
            if (target - nums[i]) in seen:
                res.append(i)
                res.append(seen[target - nums[i]])
            seen[nums[i]] = i
        res.sort()
        return res

        
