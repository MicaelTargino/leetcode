def group_anagrams(strs):
    anagrams = {}
    for word in strs:
        key = tuple(sorted(word))
        if key not in anagrams:
            anagrams[key] = []
        anagrams[key].append(word)
    return list(anagrams.values())

if __name__ == "__main__":
    # Test cases
    test_cases = [
        {
            "input": ["eat", "tea", "tan", "ate", "nat", "bat"],
            "expected": [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
        },
        {
            "input": [""],
            "expected": [[""]]
        },
        {
            "input": ["a"],
            "expected": [["a"]]
        },
        {
            "input": ["abc", "bca", "cab", "bac"],
            "expected": [["abc", "bca", "cab", "bac"]]
        },
    ]

    # Run tests
    for idx, test_case in enumerate(test_cases, 1):
        input_strs = test_case["input"]
        expected = test_case["expected"]
        result = group_anagrams(input_strs)
        assert sorted([sorted(group) for group in result]) == sorted([sorted(group) for group in expected]), \
            f"Test case {idx} failed: {result} != {expected}"
        print(f"Test case {idx} passed.")
