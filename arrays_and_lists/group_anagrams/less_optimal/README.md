# approach
    I decided to create an empty control array and start iterating over the strs array. For each string, check if there's a inner-array in the control array that contains one anagram of this string, append it to the inner-array, if not, append it in a new inner-array in the control array. Return the control array.

# Perfomance

- Time Complexity: O(m^2 x n) 
- Space Complexity: O(m x n)

# Code
```python


def isAnagram(str1: str, str2: str) -> bool: 
    if len(str1) != len(str2): return False

    char_count = {}

    for i in range(len(str1)): 
        char_count[str1[i]] = char_count.get(str1[i], 0) + 1
        char_count[str2[i]] = char_count.get(str2[i], 0) - 1

    try:
        return not max(list(char_count.values())) 
    except ValueError:  # in case of empty strings
        return True

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        control_arr = []
        for i in strs:
            inserted = False
            for j in control_arr:
                if isAnagram(i, j[0]):
                    j.append(i)
                    inserted = True
                    break
            if inserted == False:
                control_arr.append([i])

        return control_arr
```