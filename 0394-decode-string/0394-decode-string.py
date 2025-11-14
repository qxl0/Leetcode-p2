class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for ch in s:
            if ch != ']':
                stack.append(ch)
            else:
                ret = ""
                while stack[-1] != '[':
                    ret = stack.pop() + ret
                stack.pop()

                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                stack.append(ret*int(k))
        return "".join(stack)

