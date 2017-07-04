#include <stdio.h>

#define N 20

int
main() {
    int n = N;
    int c = n * n;
    int out = 1;
    int x = 0, y = 0, i;
    int a[N][N] = {0};

    while (out <= c) {
        for (i=x; i<n-x-1; i++) a[x][i] = out++;
        for (i=y; i<n-y-1; i++) a[i][n-1-y] = out++;
        for (i=n-1-x; i>x; i--) a[n-1-x][i] = out++;
        for (i=n-1-y; i>y; i--) a[i][y] = out++;
        x++;
        y++;
        if (x >= n/2) { 
            a[x][y] = out;
            break;
        }
    }


    for (x=0; x<n; x++) {
        for (y=0; y<n; y++) {
            printf("%3d ", a[x][y]);
        }
        printf("\n");
    }

    return 0;
}
