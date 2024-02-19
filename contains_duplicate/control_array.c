// using an control array to store the appeared values (On^2)
int containsDuplicate(int* nums, int numsSize) {
    int appeared[numsSize], i, j, k;
    int length, number;

    for (k = 0; k < numsSize; k++) {
        appeared[k] = -1;
    }

    for(i = 0; i < numsSize; i++) {
        length = sizeof(appeared) / sizeof(int);
        printf("%d\n", length);
        number = nums[i];

        for(j=0; j < length; j++) {
            if(appeared[j] == number) {
                return 1;
            }
        }
        int appeared_size = 0;
        for (int l = 0; l < numsSize; l++) {
            if (appeared[l] != -1) {
                appeared_size++;
            }
        }
        printf("%d", nums[i]);
        appeared[appeared_size] = nums[i];
    }
    return 0;
}