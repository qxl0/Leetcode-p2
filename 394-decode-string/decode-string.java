class Solution {
    public String decodeString(String s) {
        Stack<Integer> counts = new Stack<>();
        Stack<String> results = new Stack<>();
        
        String res = "";
        int idx = 0;

        while (idx < s.length()) {
            if (Character.isDigit(s.charAt(idx))) {
                int count = 0;
                while (Character.isDigit(s.charAt(idx))) {
                    count = count * 10 + (s.charAt(idx)-'0');
                    idx += 1;
                }
                counts.push(count);                
            }
            else if (s.charAt(idx)=='[') {
                results.push(res);
                res = "";
                idx += 1;
            }
            else if (s.charAt(idx)==']') {
                StringBuilder tmp = new StringBuilder(results.pop());
                int count = counts.pop();
                for (int i=0; i<count; i++) {
                    tmp.append(res);
                }
                res = tmp.toString();
                idx += 1;
            }
            else {
                res += s.charAt(idx);
                idx += 1;
            }
        }

        return res;
    }
}