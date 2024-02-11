import java.util.Stack;

class Solution {
    public static void main(String[] args) {
        Solution sol = new Solution();
        String s = "3[a]2[bc]";
        System.out.println(sol.decodeString2(s)); // "aaabcbc"
    }

    public String decodeString(String s) {
        Stack<Integer> counts = new Stack<>();
        Stack<String> result = new Stack<>();
        String res = "";
        int index = 0;

        while(index < s.length()){
            if(Character.isDigit(s.charAt(index))){
                int count = 0;
                while(Character.isDigit(s.charAt(index))){
                    count = 10 * count + (s.charAt(index) - '0');
                    index ++;
                }
                counts.push(count);
            }else if(s.charAt(index) == '['){
                result.push(res);
                res = "";
                index++;
            }else if(s.charAt(index) == ']'){
                StringBuilder temp = new StringBuilder(result.pop());
                int count = counts.pop();
                for(int i=0; i<count; i++){
                    temp.append(res);
                }
                res = temp.toString();
                index++;
            }else{
                res += s.charAt(index);
                index++;
            }
        }

        return res;
    }

    public String decodeString2(String s) {
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
                StringBuilder tmp = new StringBuilder();
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
    // add main function to test
   
}