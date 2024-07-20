// nested loops solution O(n^2)
int containsDuplicate(int* nums, int numsSize) {
    for (int i =0; i < numsSize; i++) {
        for (int j = 0; j < numsSize; j++) {
            if (i != j) {
                if (nums[i] == nums[j]) return 1;
            }
        }
    }
    return 0;
}
