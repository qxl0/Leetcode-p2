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
    public ListNode FrequenciesOfElements(ListNode head) {
        Dictionary<int,int> count = new();
        while (head!=null) {
            if (!count.ContainsKey(head.val)) {
                count[head.val] = 0;
            }
            count[head.val] += 1;
            head = head.next;
        }

        ListNode dummy = new();
        ListNode cur = dummy;

        foreach (var item in count) {
            int freq = item.Value;
            cur.next = new ListNode(freq);
            cur = cur.next;
        }

        return dummy.next;
    }
}