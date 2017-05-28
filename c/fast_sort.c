#include <stdio.h>


static void
_swap(int *a, int i, int j) {
    int temp = a[i];
    a[i] = a[j];
    a[j] = temp;
}

int
partion(int *a, int start, int end) {
    int temp = a[end];
    int i = start, j = end-1, p;

    while (i < j) {
        while (i<j && a[i]<=temp) i++;
        while (j>i && a[j]>temp) j--;
        _swap(a, i, j);
    }

    if (a[i] <= temp) p = i + 1;
    else p = i;

    _swap(a, p, end);

    return p;
}

void print(int *a, int start, int end) {
    int i;
    for (i=start; i<=end; i++) {
        printf("%d ", a[i]);
    }
    printf("\n");
}

void
fast_sort(int *a, int start, int end) {
    int p;
    print(a, start, end);
    if (start < end) {
        p = partion(a, start, end);
        fast_sort(a, start, p-1);
        fast_sort(a, p+1, end);
    }
}



int
main() {
    //int a[] = {0, 4, 1, 3, 2, 16, 9, 10, 14, 8, 7};
    //int a[] = {0, 16, 4, 10, 14, 7, 9, 3, 2, 8, 1};
    //int a[] = {0, 1, 4, 10, 14, 7, 9, 3, 2, 8, 16};
    int a[] = {1, 0, 1, 1, 1, 2, 4, 5, 1, 1, 1, 3, 4, 5, 6, 7, 9};
    //int a[] = {1};
    int len = sizeof(a)/sizeof(int);
    print(a, 0, len-1);
    fast_sort(a, 0, len-1);
    print(a, 0, len-1);
}
