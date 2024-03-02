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
    public string GameResult(ListNode head) {
        int odd=0,even=0;

        int i=0;
        while (head!=null && head.next!=null) {
            if (head.val>head.next.val) even+=1;
            else if (head.val<head.next.val) odd += 1;

            head = head.next.next;            
        }

        if (odd > even) {
            return "Odd";
        } else if (odd < even) {
            return "Even";
        } else {
            return "Tie";
        }
    }
}