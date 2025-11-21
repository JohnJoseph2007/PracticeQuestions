class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        ss = []
        for i in range(0,len(s)):
            x = s[i:]
            if x.count(s[i]) >= 2:
                start = x.find(s[i])
                end = x.rfind(s[i])
                for j in x[start+1:end]:
                    if s[i]+j+s[i] not in ss:
                        ss.append(s[i]+j+s[i])
        return len(ss)
    
# Submitted this code, but didn't work for all test cases, as it is not efficient for very long test case string inputs (Time limit exceeded).
# Could try to optimize it further, or change approach entirely.