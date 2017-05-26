#include <stdio.h>


int find(int *a, int length, int x) {
    int start = 0;
    //int end = sizeof(a)/sizeof(int) - 1;
    int end = length - 1;
    int mid = -1;
    
    printf("end: %d\n", end);
    while (start <= end) {
        mid = (start+end)/2;
        printf("mid: %d\n", mid);
        if (x == a[mid]) {
            if (mid>0 && a[mid]==a[mid-1]) end = mid - 1;
            else break;
        }
        if (x > a[mid]) start = mid + 1;
        if (x < a[mid]) end = mid - 1;
    }

    if (start>end && x>a[mid]) mid += 1;

    return mid;
}


int main() {
    //int a[] = {0, 1, 1, 4, 6};
    int a[] = {4};
    printf("%d\n", find(a, sizeof(a)/sizeof(int), -1));
    printf("%d\n", find(a, sizeof(a)/sizeof(int), 1));
    printf("%d\n", find(a, sizeof(a)/sizeof(int), 3));
    printf("%d\n", find(a, sizeof(a)/sizeof(int), 7));


    return 0;
}
