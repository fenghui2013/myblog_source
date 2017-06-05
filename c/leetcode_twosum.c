/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target) {
    int i, j;
    int *res = (int *)malloc(sizeof(int)*2);
    
    for (i=0; i<numsSize; i++) {
        for (j=i+1; j<numsSize; j++) {
            if ((nums[i]+nums[j]) != target) continue;
            res[0] = i;
            res[1] = j;
            goto end;
        }
    }
end:
    return res;
}


/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

int* twoSum(int* nums, int numsSize, int target) {
    int i, j, temp;
    int *res = (int *)malloc(sizeof(int)*2);
    
    for (i=0; i<numsSize; i++) {
        temp = target - *(nums+i);
        for (j=i+1; j<numsSize; j++) {
            if (*(nums+j) != temp) continue;
            res[0] = i;
            res[1] = j;
            goto end;
        }
    }
end:
    return res;
}
