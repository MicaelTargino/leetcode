# Intuition
I remembered that sets can't store duplicates

# Approach
I decided to convert the given list into a set. If the number of elements remains the same, it indicates that the list already contained only unique elements. However, if the length of the set differs from that of the list, it means that the list had duplicates.

# Perfomance

- Complexity: O(n)

- Runtime: 423ms (beats 98.50% of python users)
<img src="./img/runtime.png">

- Memory usage: 32.81 MB 


# Code
```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set_of_nums = set(nums)
        return len(set_of_nums) != len(nums)
```
