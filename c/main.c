#include <stdio.h>
#include "list.h"

int main() {
    List *list = list_create(10);
    list_print(list);
    list_revert(list);
    list_print(list);
    list_free(list);

    return 0;
}
