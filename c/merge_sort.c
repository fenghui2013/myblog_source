#include <stdio.h>
#include <stdlib.h>

void print(int *a, int start, int end) {
    int i;
    for (i=start; i<=end; i++) {
        printf("%d ", a[i]);
    }
    printf("\n");
}

void
merge(int *src, int *temp, int start, int mid, int end) {
    int i=start, j=mid+1;
    int k = start;

    while (i<=mid && j<=end) {
        if (src[i] <= src[j]) temp[k++] = src[i++];
        else temp[k++] = src[j++];
    }

    while (i <= mid) temp[k++] = src[i++];

    while (j <= end) temp[k++] = src[j++];

    while (start <= end) {
        src[start] = temp[start];
        start += 1;
    }
}

void
merge_sort(int *src, int *temp, int start, int end) {
    int mid;

    if (start < end) {
        mid = (start+end)/2;
        merge_sort(src, temp, start, mid);
        merge_sort(src, temp, mid+1, end);
        printf("%d\n", mid);
        merge(src, temp, start, mid, end);
    }
}



int
main() {
    //int a[] = {0, 4, 1, 3, 2, 16, 9, 10, 14, 8, 7};
    //int a[] = {0, 16, 4, 10, 14, 7, 9, 3, 2, 8, 1};
    //int a[] = {0, 1, 4, 10, 14, 7, 9, 3, 2, 8, 16};
    //int a[] = {1, 0, 1, 1, 1, 2, 4, 5, 1, 1, 1, 3, 4, 5, 6, 7, 9};
    //int a[] = {1};
    //int a[] = {0, 0, 0, 1, 0, 0, 0};
    //int a[] = {5, 4, 3, 2, 1};
    //int a[] = {1, 0};
    int a[] = {10, 4, 6, 3, 8, 2, 5, 7};
    int len = sizeof(a)/sizeof(int);
    int *b = (int *)malloc(sizeof(int)*len);
    print(a, 0, len-1);
    merge_sort(a, b, 0, len-1);
    print(a, 0, len-1);
}
