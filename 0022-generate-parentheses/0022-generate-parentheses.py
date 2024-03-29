class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def fun(start, end, str):
            if start == 0:
                while end!=0:
                    str += ')'
                    end-=1
                res.append(str)
            else:
                fun(start-1,end,str + '(')
                if start < end:
                    fun(start, end-1, str + ')')
        fun(n,n,'')
        return res        