#include <stdio.h>

int
len(char *s) {
    int len = 0;
    while (s[len++]);
    return len-1;
}

int myAtoi(char* str) {
    int x = 1;
    int num = 0;
    int i;
    for (i=len(str)-1; i>=0; i--) {
        if (str[i]>'9' || str[i]<'0') return -1;
        num += ((str[i]-'0')*x);
        x *= 10;
    }

    return num;
}

int main() {
    char *s = "123";
    printf("%d\n", myAtoi(s));
}
