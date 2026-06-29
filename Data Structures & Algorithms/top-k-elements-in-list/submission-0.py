class Solution:
    #return elem can be in any order
    #nums.len >= 1
    #k is at least 1
    # k is less than or equal to the number of unique elem in nums
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        bucket = [[]for _ in range(len(nums) + 1)]

        for num, freq in count.items():
            bucket[freq].append(num)
        
        result = []

        for freq in range(len(bucket) - 1, 0, -1):
            for num in bucket[freq]:
                result.append(num)

                if len(result) == k:
                    return result
        