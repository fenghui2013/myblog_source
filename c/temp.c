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
