class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        seen = set()
        last = {c:i for i,c in enumerate(s)}
        for i, ch in enumerate(s):
            if ch in seen: continue
            while stack and stack[-1]> ch and last[stack[-1]]>i:
                seen.remove(stack.pop())
                
            stack.append(ch)
            seen.add(ch)
        return "".join(stack)
            