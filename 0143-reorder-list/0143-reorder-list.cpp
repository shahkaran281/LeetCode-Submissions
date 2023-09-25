/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    void reorderList(ListNode* head) {
        if(!head || !head->next){
            return;
        }
        ListNode *slow = head,*fast = head;
        while(fast && fast->next){
            fast = fast->next->next;
            if(fast){

            slow = slow->next;
            }
        }
        ListNode* right = slow->next;
        slow->next  = NULL;
        stack <ListNode*> stk;
        while(right){
            stk.push(right);
            right = right->next;
        }
        slow = head;
        while(!stk.empty()){
            ListNode* newNode = stk.top();
            stk.pop();
            newNode->next = slow->next;
            slow->next = newNode;
            slow = newNode->next;
        }
    }
};