class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        letters = set(s) # Creates a set of unique letters in the string
        ans = 0 # Final answer
        for letter in letters: # for each unique letter in the set
            i, j = s.index(letter), s.rindex(letter) # Find first and last occurrence of the letter
            between = set() # Empty set to store unique letters between the two index constraints
            for k in range(i + 1, j): # Iterate through string between two indices
                between.add(s[k]) # Add unique letters to the set
            ans += len(between)
            print(ans)
        return ans
    
# Crazy solution
# Why does it work?
# Let test case be "bbcbaba"
# letters = {'c', 'a', 'b'} (in whichever order, can't say)
# for 'c':
# i = 2, j = 2
# between = {}
# ans = 0 + 0 = 0
# for 'a':
# i = 4, j = 6
# substring = "b"
# between = {'b'}
# ans = 0 + 1 = 1
# for 'b':
# i = 0, j = 5
# substring = "bcba"
# between = {'c', 'b', 'a'}
# ans = 1 + 3 = 4
# return 4
# BOOM!