class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numDict = {}
        for i in range(len(numbers)):
            if target - numbers[i] in numDict:
                return [numDict[target - numbers[i]], i + 1]
            else:
                numDict[numbers[i]] = i + 1
        
        return []