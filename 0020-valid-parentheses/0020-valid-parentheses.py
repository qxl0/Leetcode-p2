class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch in "({[":
                stack.append(ch)
            elif ch == ')':
                if not stack or stack[-1]!='(':
                    return False
                stack.pop()
            elif ch == '}':
                if not stack or stack[-1]!='{':
                    return False
                stack.pop()
            elif ch == ']':
                if not stack or stack[-1]!='[':
                    return False
                stack.pop()
        return len(stack)==0