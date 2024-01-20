/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode[] splitListToParts(ListNode head, int k) {
        ListNode dummy = new ListNode(-1,head);
        int len = getLen(head);
        int psize = len/k, remaining = len%k;

        ListNode[] ret = new ListNode[k];

        ListNode cur = head;
        for (int i=0;i<k;i++) {
            ret[i] = cur;
            cur = moveNext(cur, psize, remaining);
            if (remaining>0)
                remaining -= 1;
        }

        return ret;
    }

    private ListNode moveNext(ListNode cur, int psize, int remain) {
        ListNode prev = null;
        int steps = psize;
        if (remain>0)
            steps += 1;
        while (steps>0 && cur!=null){
            steps -= 1;
            prev = cur;
            cur = cur.next;
        }
        if (prev!=null)
            prev.next = null;
        return cur;
    }

    private int getLen(ListNode node) {
        int ret = 0;
        while (node!=null) {
            node = node.next;
            ret += 1;
        }
        return ret;
    }
}