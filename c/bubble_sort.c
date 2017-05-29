#include <stdio.h>

static void
_swap(int *a, int i, int j) {
    int temp = a[i];
    a[i] = a[j];
    a[j] = temp;
}

void
bubble_sort(int *a, int start, int end) {
    int i, j;

    for (i=start; i<end; i++) {
        for (j=end; j>i; j--) {
            if (a[j] < a[j-1]) _swap(a, j, j-1);
        }
    }
}

void print(int *a, int start, int end) {
    int i;
    for (i=start; i<=end; i++) {
        printf("%d ", a[i]);
    }
    printf("\n");
}


int
main() {
    //int a[] = {0, 1, 4, 10, 14, 7, 9, 3, 2, 8, 16};
    //int a[] = {1, 0, 1, 1, 1, 2, 4, 5, 1, 1, 1, 3, 4, 5, 6, 7, 9};
    //int a[] = {1};
    //int a[] = {0, 0, 0, 1, 0, 0, 0};
    int a[] = {5, 4, 3, 2, 1};
    int len = sizeof(a)/sizeof(int);
    print(a, 0, len-1);
    bubble_sort(a, 0, len-1);
    print(a, 0, len-1);

    return 0;
}
