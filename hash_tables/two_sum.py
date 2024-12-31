def two_sum(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return []

if __name__ == "__main__":
    # Test cases
    test_cases = [
        {"nums": [2, 7, 11, 15], "target": 9, "expected": [0, 1]},
        {"nums": [3, 2, 4], "target": 6, "expected": [1, 2]},
        {"nums": [3, 3], "target": 6, "expected": [0, 1]},
        {"nums": [1, 2, 3, 4, 5], "target": 10, "expected": []},  # No solution
        {"nums": [-1, -2, -3, -4, -5], "target": -8, "expected": [2, 4]},
    ]

    # Running tests
    for idx, test_case in enumerate(test_cases, 1):
        nums = test_case["nums"]
        target = test_case["target"]
        expected = test_case["expected"]
        result = two_sum(nums, target)
        assert result == expected, f"Test case {idx} failed: {result} != {expected}"
        print(f"Test case {idx} passed.")
