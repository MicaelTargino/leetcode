#! thats incomplete. Just storing to not lose the code.
def isAnagram(str1: str, str2: str) -> bool: 
    if len(str1) != len(str2): return False

    char_count = {}

    for i in range(len(str1)): 
        char_count[str1[i]] = char_count.get(str1[i], 0) + 1
        char_count[str2[i]] = char_count.get(str2[i], 0) - 1
    
    for count in char_count.values():
        if count != 0:
            return False
    
    return True

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        control_arr = 
        for i in strs:
            
    