class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        postfix = []
        res = []

        start = 1
        prefix.append(start)
        for num in nums[:-1]:
            prefix.append(num * prefix[-1])
        start = 1
        postfix.append(start)
        for i in range(len(nums) - 1, 0, -1):
            postfix.append(nums[i] * postfix[-1])
        
        postfix.reverse()
        for i in range(len(nums)):
            res.append(prefix[i] * postfix[i])
        
        return res
