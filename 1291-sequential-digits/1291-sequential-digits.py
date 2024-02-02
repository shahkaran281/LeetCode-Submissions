class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        def fun(x):
            strX = str(x)
            k = int(strX[0])
            for i in range(1,len(strX)):
                k+=1
                if k == 10:
                    return -1
                strX = strX[:i] + str(k) + strX[i+1:]
            return int(strX)
        res = []
        base = pow(10,floor(log10(low)))
        curr = base
        while curr <= high:
            val = fun(curr)
            if val >= low and val <= high and val not in res:
                res.append(val)
            if curr == 10 * base:
                base = curr
            else:
                curr+=base
        # ans = res.sort()
        return sorted(res)
        