class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        for ch in s:
            if ch.isdigit():
                buf = []
                while stack and stack[-1].isdigit():
                    buf.append(stack.pop())
                # when stop 
                if stack:
                    stack.pop()
                else:
                    for b in buf:
                        stack.append(b)
                    stack.append(ch)
            else:
                stack.append(ch)
        return "".join(stack)

