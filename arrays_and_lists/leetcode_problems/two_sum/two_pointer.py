class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums = sorted(nums)

        first_pointer = 0
        last_pointer = len(nums) - 1
        while(True):
            if nums[first_pointer] + nums[last_pointer] > target:
                last_pointer -= 1

            elif nums[first_pointer] + nums[last_pointer] < target:
                first_pointer += 1
            
                return [nums[first_pointer], nums[last_pointer]]