#include <stdio.h>
#include <stdlib.h>

#include "list.h"


struct Node {
    int value;
    Node *next;
};

struct List {
    Node *head;
    int count;
};

List* list_create(int count) {
    List *list = (List *)malloc(sizeof(List));
    list->count = count;
    list->head = (Node *)malloc(sizeof(Node));
    list->head->next = NULL;
    list->head->value = 0;

    if (count <= 0) {
        list->count = 0;
        return list;
    }
    Node *temp = list->head;
    for (int i=0; i<count; i++) {
        Node *node = (Node *)malloc(sizeof(Node));
        node->value = i;
        node->next = NULL;
        temp->next = node;
        temp = node;
    }
    return list;
}

void list_revert(List *list) {
    Node *new_head = NULL;
    Node *head = list->head->next;
    Node *temp = head;
    while (head != NULL) {
        head = head->next;
        temp->next = new_head;
        new_head = temp;
        temp = head;
    }
    list->head->next = new_head;
}

void list_print(List *list) {
    Node *temp = list->head->next;
    while (temp != NULL) {
        printf("%d ", temp->value);
        temp = temp->next;
    }
    printf("\n");
}

void list_free(List *list) {
    Node *head = list->head;
    while (head != NULL) {
        Node * temp = head;
        head = head->next;
        free(temp);
    }

    free(list);
}
