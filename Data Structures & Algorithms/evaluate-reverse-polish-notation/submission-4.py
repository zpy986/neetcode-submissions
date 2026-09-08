class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in ("+", "-", "*", "/") and stack:
                ope2 = int(stack.pop())
                ope1 = int(stack.pop())
                optr = token
                if optr == "+":
                    res = ope1 + ope2
                elif optr == "-":
                    res = ope1 - ope2
                elif optr == "*":
                    res = ope1 * ope2
                else:
                    res = int(ope1 / ope2)
                stack.append(str(res))
            else:
                stack.append(token)

        return int(stack.pop())


