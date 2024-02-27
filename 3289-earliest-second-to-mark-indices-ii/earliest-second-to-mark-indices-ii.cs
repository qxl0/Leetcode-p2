public class Solution {
    int[] A;
    long Asum;
    public int EarliestSecondToMarkIndices(int[] A, int[] B) {
        this.A = A;
        // Console.WriteLine($"A={A[0]}");
        Asum = 0;
        foreach (var a in A) {
            Asum += a;
        }
        // Console.WriteLine($" here");
        Dictionary<int,int> firsts = new();
        for (int i=0;i<B.Length;i++) {
            int b = B[i];
            if (A[b-1]>0 && !firsts.ContainsKey(b)) {
                firsts[b] = i;
            }
        }

        Dictionary<int,int> firsts_inv = new();
        foreach (var (b,i) in firsts) {
            firsts_inv[i] = b;
        }

        long lo =0, hi = B.Length+1;
        while (lo<hi) {
            long mi = lo+(hi-lo)/2;
            if (checkok(mi, firsts_inv)) {
                hi = mi;            
            }
            else {
                lo = mi + 1;
            }
        }

        return lo<=B.Length? (int)lo:-1;
    }

    private bool checkok(long bound, Dictionary<int,int> firsts_inv) {
        // is B[:bound] enough to clear A
        // Console.WriteLine($"bound={bound}");
        PriorityQueue<int,int> pq = new();
        long mark = 0;
        for (long i=bound-1;i>=0;i--) {
            if (firsts_inv.ContainsKey((int)i)) {
                int eleA = A[firsts_inv[(int)i]-1];
                pq.Enqueue(eleA, eleA);
                if (mark>0) mark -=1;
                else {
                    mark += 1;
                    pq.Dequeue();
                }
            }
            else mark += 1;
        }
        long pq_sum = getSum(pq);
        return Asum-pq_sum+A.Length-pq.Count<=mark;
    }

    private long getSum(PriorityQueue<int,int> pq) {
        PriorityQueue<int,int> pq_copy = new PriorityQueue<int,int>(pq.UnorderedItems); 
        long sum = 0;
        while (pq_copy.Count > 0) 
            sum += pq_copy.Dequeue();
        
        return sum;
    }
}