public class StockSpanner {
    Stack<(int,int)> stack; // (value, span)
    public StockSpanner() {
        stack = new Stack<(int,int)>();
    }
    
    public int Next(int price) {
        int span = 1;
        while (stack.Count>0 && stack.Peek().Item1<=price) {
            var psan = stack.Pop().Item2;
            span += psan;
        }

        stack.Push((price,span));

        return span;
    }
}

/**
 * Your StockSpanner object will be instantiated and called as such:
 * StockSpanner obj = new StockSpanner();
 * int param_1 = obj.Next(price);
 */