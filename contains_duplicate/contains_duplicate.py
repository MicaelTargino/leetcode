class Solution:
    def containsDuplicate(self, nums):
        set_of_nums = set(nums)
        return len(set_of_nums) != len(nums)