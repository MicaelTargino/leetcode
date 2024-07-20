import random
import time

def gererate_random_unsorted_list(length: int) -> "List['int']":
    list = [] 
    for i in range(length):
        list.append(random.randint(0, length))
    return list

def swap(lst, i, j):
    k = lst[j] 
    lst[j] = lst[i]
    lst[i] = k
    return lst

def insertion_sort(arr: "List[int]"):
    n = len(arr)

    if n <= 1: # if arr has 0-1 elements, it is already sorted
        return 

    for i in range(1, n): # start iteration from second element
        current = arr[i] # store in memory the current element

        j = i - 1 # decrementation index 
        while j >= 0 and current < arr[j]: 
            arr[j+1] = arr[j] # swipe right 
            j = j - 1
        
        # add current element in the right position (after there is no more smaller elements)
        arr[j+1] = current
        
def main():
    random_length = random.randint(5,15)
    unsorted_list = gererate_random_unsorted_list(random_length)

    print(f'list of {random_length} unsorted elements generated')

    print(unsorted_list)

    start_time = time.time()
    insertion_sort(unsorted_list)    
    
    print(f'list sorted in : {(time.time() - start_time)} seconds')

    print(unsorted_list)


if __name__ == "__main__":
    main()