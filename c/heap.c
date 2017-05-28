#include <stdio.h>
#include <stdlib.h>

#define PARENT(i) (i)/2
#define LEFT(i) 2*(i)
#define RIGHT(i) 2*(i)+1


typedef struct heap {
    int *a;
    int length;
    int size;
} heap;

heap* heap_create(int size);
int   heap_insert(heap *h, int key);
int   heap_set_key(heap *h, int i, int key);
int   heap_get_max(heap *h);
int   heap_max(heap *h);
//void heap_sort(heap *h);
void  heap_release(heap *h);

static void
_swap(int *a, int i, int j) {
    int temp = a[i];
    a[i] = a[j];
    a[j] = temp;
}

void
max_heapify(int *a, int size, int i) {
    int l = LEFT(i);
    int r = RIGHT(i);
    int max = i;
    if (l<=size && a[l]>a[i]) max = l;
    if (r<=size && a[r]>a[max]) max = r;
    if (max != i) {
        _swap(a, i, max);
        max_heapify(a, size, max);
    }
}

heap*
heap_create(int size) {
    heap *h = (heap *)malloc(sizeof(heap));
    h->length = size+1;
    h->a = (int *)malloc(sizeof(int)*h->length);
    h->size = 0;

    return h;
}

/**
 * -1 error: heap is full
 * 0  success
 */
int
heap_insert(heap *h, int key) {
    if (h->size == h->length-1) return -1;
    h->size += 1;
    heap_set_key(h, h->size, key);
    return 0;
}

int
heap_set_key(heap *h, int i, int key) {
    int *temp = h->a;
    temp[i] = key;
    while (i>1 && temp[PARENT(i)] < temp[i]) {
        _swap(temp, PARENT(i), i);
        i = PARENT(i);
    }
    return 0;
}

/*
 * -1 error: heap is empty
 * max result 
 */
int
heap_get_max(heap* h) {
    if (h->size == 0) return -1;
    int max = h->a[1];
    _swap(h->a, 1, h->size);
    h->size -= 1;
    max_heapify(h->a, h->size, 1);

    return max;
}

int
heap_max(heap *h) {
    if (h->size == 0) return -1;
    return h->a[1];
}

void 
heap_release(heap *h) {
    free(h->a);
    free(h);
    h = NULL;
}


/*
static void
_build_heap(int *a, int size) {
    int i;
    for (i=size/2; i>0; i--) {
        max_heapify(a, size, i);
    }
}

void
heap_sort(int *a, int size) {
    int i;

    _build_heap(a, size);
    for (i=size; i>=2; i--) {
        _swap(a, 1, i);
        max_heapify(a, i-1, 1);
    }
}
*/

void print(int *a, int size) {
    int i;
    for (i=1; i<=size; i++) {
        printf("%d ", a[i]);
    }
    printf("\n");
}

int main() {
    //int a[] = {0, 4, 1, 3, 2, 16, 9, 10, 14, 8, 7};
    //int a[] = {0, 16, 4, 10, 14, 7, 9, 3, 2, 8, 1};
    //int a[] = {0, 1, 4, 10, 14, 7, 9, 3, 2, 8, 16};
    //int size = sizeof(a)/sizeof(int)-1;
    //print(a, size);
    //build_heap(a, size);
    //print(a, size);
    //heap_sort(a, size);
    //print(a, size);
    
    heap *h = heap_create(10);
    printf("heap_insert: %d\n", heap_insert(h, 4));
    printf("heap_insert: %d\n", heap_insert(h, 1));
    printf("heap_insert: %d\n", heap_insert(h, 3));
    printf("heap_insert: %d\n", heap_insert(h, 2));
    printf("heap_insert: %d\n", heap_insert(h, 16));
    printf("heap_insert: %d\n", heap_insert(h, 9));
    printf("heap_insert: %d\n", heap_insert(h, 10));
    printf("heap_insert: %d\n", heap_insert(h, 14));
    printf("heap_insert: %d\n", heap_insert(h, 8));
    printf("heap_insert: %d\n", heap_insert(h, 7));
    printf("heap_insert: %d\n", heap_insert(h, 100));

    printf("heap_set_key: %d\n", heap_set_key(h, 1, 100));
    
    printf("heap_get_max: %d\n", heap_get_max(h));
    printf("heap_get_max: %d\n", heap_get_max(h));
    printf("heap_get_max: %d\n", heap_get_max(h));
    printf("heap_get_max: %d\n", heap_get_max(h));
    printf("heap_get_max: %d\n", heap_get_max(h));
    printf("heap_get_max: %d\n", heap_get_max(h));
    printf("heap_get_max: %d\n", heap_get_max(h));
    printf("heap_get_max: %d\n", heap_get_max(h));
    printf("heap_get_max: %d\n", heap_get_max(h));
    printf("heap_get_max: %d\n", heap_get_max(h));
    printf("heap_get_max: %d\n", heap_get_max(h));

    heap_release(h);

    return 0;
}
