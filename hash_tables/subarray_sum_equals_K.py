def subarray_sum(nums, k):
    prefix_sum_map = {0: 1}
    current_sum = 0
    count = 0

    for num in nums:
        current_sum += num
        if current_sum - k in prefix_sum_map:
            count += prefix_sum_map[current_sum - k]
        prefix_sum_map[current_sum] = prefix_sum_map.get(current_sum, 0) + 1

    return count

if __name__ == "__main__":
    # Test cases
    test_cases = [
        {"nums": [1, 1, 1], "k": 2, "expected": 2},  # Two subarrays: [1,1], [1,1]
        {"nums": [1, 2, 3], "k": 3, "expected": 2},  # Two subarrays: [1,2], [3]
        {"nums": [1, -1, 1], "k": 1, "expected": 3}, # Three subarrays: [1], [1,-1,1], [1]
        {"nums": [1], "k": 0, "expected": 0},        # No subarrays
        {"nums": [0, 0, 0, 0], "k": 0, "expected": 10}, # All possible subarrays
    ]

    # Run tests
    for idx, test_case in enumerate(test_cases, 1):
        nums = test_case["nums"]
        k = test_case["k"]
        expected = test_case["expected"]
        result = subarray_sum(nums, k)
        print(f"Test Case {idx} - nums: {nums}, k: {k}, Result: {result}, Expected: {expected}")
        assert result == expected, f"Test case {idx} failed: {result} != {expected}"
        print(f"Test case {idx} passed.")
