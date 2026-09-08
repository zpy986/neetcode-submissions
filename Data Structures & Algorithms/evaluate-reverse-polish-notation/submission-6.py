class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in ("+", "-", "*", "/"):
                ope2 = stack.pop()
                ope1 = stack.pop()
                if token == "+":
                    res = ope1 + ope2
                elif token == "-":
                    res = ope1 - ope2
                elif token == "*":
                    res = ope1 * ope2
                else:
                    res = int(ope1 / ope2)
                stack.append(res)
            else:
                stack.append(int(token))

        return stack.pop()


