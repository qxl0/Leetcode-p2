class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        def eval(op1,op2, ch):
            if ch == '+':
                return op2+op1
            elif ch == '-':
                return op2-op1
            elif ch == '*':
                return op2*op1
            else:
                sign = op2>0 and op1 > 0 or op2<0 and op1 <0
                ret = abs(op2)//abs(op1)
                if not sign:
                    ret = -1*ret
                return ret
        for ch in tokens:
            if ch.lstrip('+-').isnumeric():
                stack.append(int(ch))
            elif ch in "+-*/":
                op1 = stack.pop()
                print('op1:', op1, 'ch:', ch)
                op2 = stack.pop()
                stack.append(eval(op1,op2, ch))
        return stack.pop()