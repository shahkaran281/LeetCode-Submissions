class Solution:
    def simplifyPath(self, path: str) -> str:
        stk = []
        curr = ''
        
        for ch in path + '/':  
            if ch == '/':
                if curr == '..':
                    if stk:
                        stk.pop()
                elif curr != '' and curr != '.':
                    stk.append(curr)
                curr = ''
            else:
                curr += ch
        
        return '/' + '/'.join(stk)
