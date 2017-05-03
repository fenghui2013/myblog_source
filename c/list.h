#ifndef _LIST_H_
#define _LIST_H_

typedef struct Node Node;
typedef struct List List;

List* list_create(int count);
void  list_revert(List *list);
void  list_free(List *list);
void  list_print(List *list);

#endif
