# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        critical_points = []
        def iscritical(cur,prev,nxt):
            if cur.val<prev.val and cur.val<nxt.val:
                return True
            if cur.val>prev.val and cur.val>nxt.val:
                return True 
            return False 
        prev = head 
        cur = prev.next
        if not cur.next:
            return [-1,-1]
        cur_pos = 0
        while cur.next:
            if iscritical(cur,prev,cur.next):
                critical_points.append(cur_pos)
            prev = cur 
            cur = cur.next 
            cur_pos += 1
        
        # [2,4,5]
        if len(critical_points)<=1:
            return [-1,-1]
        mx = critical_points[-1]-critical_points[0]
        mn = min(y-x for x,y in zip(critical_points,critical_points[1:]))
        return [mn,mx]
        

         


