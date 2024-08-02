import random
import time

def generate_random_unsorted_list(length: int) -> list:
    return [random.randint(0, length) for _ in range(length)]

def merge(left_arr, right_arr, arr):
    left_size = len(left_arr)
    right_size = len(right_arr)
    i = l = r = 0

    # check the conditions for merging
    while l < left_size and r < right_size:
        if left_arr[l] < right_arr[r]:
            arr[i] = left_arr[l]
            l += 1
        else:
            arr[i] = right_arr[r]
            r += 1
        i += 1

    while l < left_size:
        arr[i] = left_arr[l]
        i += 1 
        l += 1

    while r < right_size:
        arr[i] = right_arr[r]
        i += 1 
        r += 1

def merge_sort(arr):
    # divide the array into subarrays until we have length 1 arrays
    n = len(arr)
    if n <= 1: 
        return  # base case

    middle = n // 2

    left_arr = arr[:middle]
    right_arr = arr[middle:]

    merge_sort(left_arr)
    merge_sort(right_arr)

    merge(left_arr, right_arr, arr)

def main():
    random_length = random.randint(5, 15)
    unsorted_list = generate_random_unsorted_list(random_length)

    print(f'List of {random_length} unsorted elements generated:')
    print(unsorted_list)

    start_time = time.time()
    merge_sort(unsorted_list)    
    end_time = time.time()

    print(f'List sorted in: {end_time - start_time:.6f} seconds')
    print(unsorted_list)

if __name__ == "__main__":
    main()
