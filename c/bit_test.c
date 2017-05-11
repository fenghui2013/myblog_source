#include <stdio.h>

/*
int count(int n) {
    int count = 0;
    unsigned int flag = 1;
    while (flag) {
        if (n & flag) count++;
        flag = flag << 1;
    }

    return count;
}
*/

int count(int n) {
    int count = 0;
    while (n) {
        count++;
        n = (n-1) & n;
    }
    return count;
}



int main() {
    printf("%d\n", count(1));
    printf("%d\n", count(2));
    printf("%d\n", count(4));
    printf("%d\n", count(8));
    printf("%d\n", count(-1));
    //printf("%d\n", count(-128));

    return 0;
}
