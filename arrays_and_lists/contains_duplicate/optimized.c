// strategie: sort the array and compare each number with the next one. -> O(n log(n))

int compare(const void*a, const void*b) {
    return (*(int*)a - *(int*)b); // if 0, the numers are equal
}

int containsDuplicate(int* nums, int numsSize) {
    qsort(nums, numsSize, sizeof(int), compare);
    for(int i = 0; i < numsSize -1; i++) {
        if (nums[i] == nums[i + 1]) {
            return 1;
        }
    }

    return 0;
}
