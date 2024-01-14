class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
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

        