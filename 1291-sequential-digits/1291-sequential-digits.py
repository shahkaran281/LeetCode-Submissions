class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        def fun(x):
            strX = str(x)
            k = int(strX[0])
            for i in range(1,len(strX)):
                k+=1
                # print(f'k: {k}')
                if k == 10:
                    # print('X : {x} index : {i}')
                    return -1
                strX = strX[:i] + str(k) + strX[i+1:]
            return int(strX)
        res = []
        base = pow(10,floor(log10(low)))
        # print(f'Base : {base}')
        curr = base
        while curr <= high:
            val = fun(curr)
            # print(f'Value : {curr} Res : {val} ')
            if val >= low and val <= high and val not in res:
                res.append(val)
            if curr == 10 * base:
                base = curr
            else:
                curr+=base
        # ans = res.sort()
        return sorted(res)
        