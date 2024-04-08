class Solution {
    public int countStudents(int[] students, int[] sandwiches) {
        Deque<Integer> dq = new LinkedList<>();
        for (var x:students) {
            dq.addLast(x);
        }

        int cur = 0;
        int count = 0;
        while (!dq.isEmpty()) {
            Integer want = dq.removeFirst();
            if (cur<sandwiches.length) {
                int sandwich = sandwiches[cur];
                if (sandwich!=want) {
                    dq.addLast(want); // put to end                     
                    count += 1;
                }
                else {
                    cur += 1;  // move to next sandwich                    
                    count = 0;
                }
                if (count >= dq.size()) {
                    break;
                }
            }
            else {
                break;
            }
        }

        return dq.size();
    }
}