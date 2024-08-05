import random
import time

def generate_random_unsorted_list(length: int) -> list:
    return [random.randint(0, length) for _ in range(length)]


def partition(arr, left, right):
    pivot = arr[right]
    i = left - 1

    for j in range(left, right):
        if arr[j] <= pivot: 
            i += 1
            arr[i], arr[j] = arr[j], arr[i] # swap items

    arr[i+1], arr[right] = arr[right], arr[i+1] # put pivot in correct position
    return i+1 #return pivot's position



def quick_sort(arr, left_ptr, right_ptr):
    if left_ptr < right_ptr:
        pivot = partition(arr, left_ptr, right_ptr)
        quick_sort(arr, left_ptr, pivot-1)
        quick_sort(arr, pivot+1, right_ptr)

def main():
    random_length = random.randint(5, 15)
    unsorted_list = generate_random_unsorted_list(random_length)

    print(f'List of {random_length} unsorted elements generated:')
    print(unsorted_list)

    start_time = time.time()
    quick_sort(unsorted_list, 0, len(unsorted_list)-1)    
    end_time = time.time()

    print(f'List sorted in: {end_time - start_time:.6f} seconds')
    print(unsorted_list)

if __name__ == "__main__":
    main()
