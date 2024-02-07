# Approach
I decided to check every combination of numbers in the list and check if their sum matches the target value

# Perfomance

- Complexity: O(n^2) 

- Runtime: 82 ms

- Memory usage: 17.27 MB (Beats 87.22% of users with Python3)

# Code
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index1, num in enumerate(nums):
            n1 = num
            for index2, n2 in enumerate(nums):
                if n1 + n2 == target and index1 != index2:
                    return [index1, index2]
        return []
```
