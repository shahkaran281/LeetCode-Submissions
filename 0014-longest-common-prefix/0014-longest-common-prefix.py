class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        for index in range(len(strs[0])):
            for i in range(1, len(strs)):
                if index >= len(strs[i]) or strs[i][index] != strs[0][index]:
                    return strs[0][:index]
        return strs[0]