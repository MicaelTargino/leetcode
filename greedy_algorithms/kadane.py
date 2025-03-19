def max_subarray_sum(arr):
    if len(arr) == 0:
        return
    
    current_sum = arr[0]
    global_sum = arr[0]

    for num in arr[1:]: 
        current_sum = max(num, current_sum + num)
        global_sum = max(current_sum, global_sum)
    
    return global_sum

if __name__ == '__main__':
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    max_sum = max_subarray_sum(arr)
    # max_sum = kadane_algorithm(arr)
    print(max_sum)
