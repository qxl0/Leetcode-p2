class Solution:
    def simplifyPath(self, path: str) -> str:
        lst = path.split('/')
        stack = []
        for i in range(len(lst)):
            if lst[i] == '.':
                continue
            elif lst[i] == '..':
                if stack:
                    stack.pop()
            elif lst[i] == '':
                continue
            else:
                stack.append(lst[i])
        ret = '/' + '/'.join(stack)
        # print(ret)
        return ret