/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
typedef struct ListNode * ListNodePointer;

struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    int c = 0;
    ListNodePointer sum = (ListNodePointer)malloc(sizeof(struct ListNode)), temp;
    sum->val = 0;
    sum->next = NULL;
    temp = sum;
    while (c || l1 || l2) {
        c += (l1?l1->val:0)+(l2?l2->val:0);
        temp->next = (ListNodePointer)malloc(sizeof(struct ListNode));
        temp->next->val = c % 10;
        temp->next->next = NULL;
        temp = temp->next;
        c /= 10;
        if(l1) l1 = l1->next;
        if(l2) l2 = l2->next;
    }
    
    return sum->next;
}
