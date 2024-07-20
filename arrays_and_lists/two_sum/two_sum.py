class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx1, num in enumerate(nums):
            n1 = num
            for idx2, n2 in enumerate(nums):
                if n1 + n2 == target and idx1 != idx2:
                    return [idx1, idx2]
        return []