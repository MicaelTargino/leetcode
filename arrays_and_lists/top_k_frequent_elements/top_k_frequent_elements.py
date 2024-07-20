class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        char_count = {}
        for n in nums:
            char_count[n] = char_count.get(n, 0) + 1

        value_key_pairs = sorted(((value, key) for (key,value) in char_count.items()), reverse=True)

        ordered_dict = {k:v for v, k in value_key_pairs}

        return_list = []

        for index, (mkey, mvalue) in enumerate(ordered_dict.items()):
            if index < k: return_list.append(mkey)

        return return_list[:k]