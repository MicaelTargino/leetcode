# Intuition
If a anagram is valid, each letter appears the same amount of times in the first and second strings.

# Approach
I decided to build a map for each given string, containing the each unique letter as a key and the amount of times it appears in the string as the value. Then iterate over the map items and checking if each letter appeared the same amount of times in both string. 

# Perfomance

- Complexity: O(n)

- Runtime: 53ms (beats 77.24% of python users)
<img src="./img/runtime.png">

- Memory usage: 17.99 MB 


# Code
```
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # t is anagram of s ? true : false
        map_s = {}
        for element in list(s):
            if map_s.get(element):
                map_s[element] = map_s[element] + 1
            else:
                map_s[element] = 1
        map_t = {}
        for element in list(t):
            if map_t.get(element):
                map_t[element] = map_t[element] + 1
            else:
                map_t[element] = 1

        if len(s) != len(t):
            return False

        for item in map_t.items():
            if map_s.get(item[0]) != item[1]:
                return False
                
        return True
```