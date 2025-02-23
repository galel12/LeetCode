from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def generate(openP, closedP):
            if openP == closedP == n:
                res.append("".join(stack))
                return
            
            if openP < n:
                stack.append("(")
                generate(openP + 1, closedP)
                stack.pop()
            if closedP < openP:
                stack.append(")")
                generate(openP, closedP + 1)
                stack.pop()
        
        generate(0,0)
        return res
