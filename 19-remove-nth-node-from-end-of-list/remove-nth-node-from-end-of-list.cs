/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
public class Solution {
    public ListNode RemoveNthFromEnd(ListNode head, int n) {
        // key is to find nth node's prev
        ListNode dummy = new ListNode(0,head); 
        ListNode prev = dummy;
        ListNode cur = head;

        while (n>0 && cur!=null) {
            cur = cur.next;
            n -= 1;
        }

        while (cur!=null && prev!=null) {
            cur = cur.next;
            prev = prev.next;
        }

        // remove 
        prev.next = prev.next.next;

        return dummy.next;

    }
}