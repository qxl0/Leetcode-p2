class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for ch in s:
            if ch=='(':
                stack.append(ch)
            elif ch == ')':
                temp = []
                while stack and stack[-1]!='(':
                    temp.append(stack.pop())
                stack.pop() # pop (
                stack.extend(temp)
            else:
                stack.append(ch)
        return "".join(stack)