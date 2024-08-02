# approach
    I decided to use a hash map to store the strings that have the same amount of each characters together in a list that is the value for the hash that contains the info about the characters and its quantities.

# Perfomance

- Time Complexity: O(k x n), where k is the number of strs list and n is the max length of a string. 
- Space Complexity: O(k x m), where k is the number of strs list and m is the max length of a string

# Code
```python
def gen_hash(mystr):
    # count the ocurrence of each character and store in the order in the char_count list
    char_count = [0] * 26  
    for char in mystr:
        char_count[ord(char) - ord('a')] += 1
    return tuple(char_count)  

class Solution:
    def groupAnagrams(self, strs):
        res = {}  # This will map the hash to the list of anagrams
        for mystr in strs:
            hash_code = gen_hash(mystr)
            if hash_code not in res:
                res[hash_code] = []
            res[hash_code].append(mystr)  # Append to the list in the dictionary
        
        return list(res.values())
```