# Intuition
If a anagram is valid, each letter appears the same amount of times in the first and second strings.

# Approach
I decided to build a map to store the number of times a letter appear, it increments the value each time the letter appears in the first string, and descreases the value each time it appears in the second string. If one string is a anagram of the other, the final result is that all the values for the letters are 0. 

# Perfomance

- Complexity: O(c), c being the number of unique characters in the strings

- Runtime: 50ms (beats 69.75% of python users)
<img src="./img/runtime.png">

- Memory usage: 17.99 MB 


# Code
```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        char_count = {}

        for i in range(len(s)):
            char_count[s[i]] = char_count.get(s[i], 0) + 1
            char_count[t[i]] = char_count.get(t[i], 0) - 1

        for count in char_count.values():
            if count != 0:
                return False

        return True
```