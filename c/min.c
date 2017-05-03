#include<stdio.h>

int min(int *array, int length) {
    if (array == NULL || length<=0) return -1;

    int start = 0;
    int end = length - 1;
    int mid = (start+end)/2;
    while (array[start] >= array[end]) {
        if (end-start == 1) {
            mid = end;
            break;
        }
        if (array[mid] >= array[start]) start = mid;
        else if (array[mid] <= array[end]) end = mid;
        mid = (start+end)/2;
    }
    return array[mid];
}

int binary_find(int *array, int length, int x) {
    int start = 0;
    int end = length - 1;
    int mid = (start+end)/2;
    while (start <= end) {
        if (array[mid] == x) return 1;
        if (x > array[mid]) start = mid+1;
        if (x < array[mid]) end = mid-1;
        mid = (start+end)/2;
    }
    return 0;
}


int find(int *array, int length, int x) {
    if (array == NULL || length<=0) return -1;

    int start = 0;
    int end = length - 1;
    int mid = (start+end)/2;
    while (start <= end) {
        //printf("%d %d %d\n", start, mid, end);
        //printf("%d %d %d\n", array[start], array[mid], array[end]);
        if (array[mid] == x) return 1;
        if (array[mid] >= array[start]) {
            if (x < array[start]) start = mid+1;
            else if (x < array[mid]) end = mid-1;
            else if (x > array[mid]) start = mid+1;
        }
        if (array[mid] < array[end]) {
            if (x > array[end]) end = mid-1;
            else if (x < array[mid]) end = mid-1;
            else if (x > array[mid]) start = mid+1;
        }
        mid = (start+end)/2;
    }
    return 0;
}

int main() {
    //int array1[12] = {14, 16, 18, 19, 1, 2, 3, 5, 8, 9, 11, 13};
    int array1[] = {8, 9, 11, 13, 14, 16, 18, 19, 1, 2, 3, 5, 6, 7};
    printf("min: %d\n", min(array1, 7));
    printf("find 14: %d\n", find(array1, sizeof(array1)/sizeof(int), 14));
    printf("find 16: %d\n", find(array1, sizeof(array1)/sizeof(int), 16));
    printf("find 19: %d\n", find(array1, sizeof(array1)/sizeof(int), 19));
    printf("find  1: %d\n", find(array1, sizeof(array1)/sizeof(int), 1));
    printf("find  8: %d\n", find(array1, sizeof(array1)/sizeof(int), 8));
    printf("find 13: %d\n", find(array1, sizeof(array1)/sizeof(int), 13));
    printf("find  7: %d\n", find(array1, sizeof(array1)/sizeof(int), 7));
    printf("liu hao tian\n");
    //int array2[7] = {1, 2, 3, 4, 6, 8, 9};
    //printf("find: %d\n", binary_find(array2, 7, 4));
    //printf("find: %d\n", binary_find(array2, 7, 6));
    //printf("find: %d\n", binary_find(array2, 7, 9));
    //printf("find: %d\n", binary_find(array2, 7, 1));
    //printf("find: %d\n", binary_find(array2, 7, 2));
    //printf("find: %d\n", binary_find(array2, 7, 3));
    //printf("find: %d\n", binary_find(array2, 7, 7));

    return 0;
}
