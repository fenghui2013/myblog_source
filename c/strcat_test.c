#include <stdio.h>
#include <string.h>

int main() {
    char s1[11] = "hello";
    char s2[] = "wor\0d";

    printf("%ld\n", strlen(s1));
    strcat(s1, s2);
    printf("%s\n", s1);
    printf("%ld\n", strlen(s1));
}
