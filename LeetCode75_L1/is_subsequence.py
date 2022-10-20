class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s:
            return True
        
        counter = 0
        for char_t in t:
            if char_t == s[counter]:
                counter += 1
            if counter == len(s):
                break
        return counter == len(s)