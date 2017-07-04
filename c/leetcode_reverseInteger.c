#include <stdio.h>
#include <stdint.h>

int reverse(int x) {
    long long rev_x = 0;
    while (x) {
        rev_x = rev_x*10 + x%10;
        x /= 10;
    }
    return (rev_x>INT32_MAX || rev_x<INT32_MIN) ? 0 : rev_x;
}

int
main() {
    printf("%d\n", reverse(123456));
}
