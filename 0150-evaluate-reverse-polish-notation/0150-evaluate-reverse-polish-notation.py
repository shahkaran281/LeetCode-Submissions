class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i in ['+','-','/','*']:
                y = stack.pop()
                x = stack.pop()
                if i == '+':
                    stack.append(x+y)
                else:
                    if i == '-':
                        stack.append(x-y)
                    else: 
                        if i == '/':
                            stack.append(int(x/y))
                        else:
                            stack.append(x*y)
            else:
                stack.append(int(i))
        return stack.pop()