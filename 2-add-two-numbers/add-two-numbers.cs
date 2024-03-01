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
    public ListNode AddTwoNumbers(ListNode l1, ListNode l2) {
        ListNode ans = new();
        int carry = 0;

        ListNode cur1 = l1, cur2 = l2;
        ListNode cur = ans;
        while (cur1!=null && cur2!=null) {
            carry += cur1.val + cur2.val;
            cur.next = new ListNode(carry%10);;
            carry /= 10;
            cur = cur.next;
            cur1 = cur1.next;
            cur2 = cur2.next;
        }

        while (cur1!=null) {
            carry += cur1.val;
            cur.next = new ListNode(carry%10);
            cur = cur.next;
            carry /= 10;
            cur1 = cur1.next;
        }

        while (cur2!=null) {
            carry += cur2.val;
            cur.next = new ListNode(carry%10);
            cur = cur.next;
            carry /= 10;
            cur2 = cur2.next;
        }

        while (carry!=0) {
            cur.next = new ListNode(carry %10);
            cur=cur.next;
            carry /=10;
        }
        return ans.next;

    }
}