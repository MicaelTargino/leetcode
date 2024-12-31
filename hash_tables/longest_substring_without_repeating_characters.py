def length_of_longest_substring(s):
    char_index = {}
    left = 0
    max_length = 0
    for right, char in enumerate(s):
        if char in char_index and char_index[char] >= left:
            left = char_index[char] + 1
        char_index[char] = right
        max_length = max(max_length, right - left + 1)
    return max_length

if __name__ == "__main__":
    # Test cases
    test_cases = [
        {"input": "abcabcbb", "expected": 3},  # "abc"
        {"input": "bbbbb", "expected": 1},    # "b"
        {"input": "pwwkew", "expected": 3},   # "wke"
        {"input": "", "expected": 0},         # ""
        {"input": " ", "expected": 1},        # " "
        {"input": "au", "expected": 2},       # "au"
        {"input": "dvdf", "expected": 3},     # "vdf"
    ]

    # Run tests
    for idx, test_case in enumerate(test_cases, 1):
        input_str = test_case["input"]
        expected = test_case["expected"]
        result = length_of_longest_substring(input_str)
        assert result == expected, f"Test case {idx} failed: {result} != {expected}"
        print(f"Test case {idx} passed.")

