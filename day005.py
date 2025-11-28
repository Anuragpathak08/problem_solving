class Solution:
    def longestPalindrome(self, s: str) -> str:
        len_s = len(s)
        reslen = (0,0,0)
        for i in range(len_s):

            l,r = i,i

            while l >= 0 and r <len_s and s[l]==s[r]:
                l-=1
                r+=1
            
            r= r-1
            l= l+1
            if (r-l+1) > reslen[2]:
                    reslen = (l, r, r-l+1)
            
            l,r = i,i+1

            while l >= 0 and r <len_s and s[l]==s[r]:
                l-=1
                r+=1

            r= r-1
            l= l+1
            if (r-l+1) > reslen[2]:
                    reslen = (l, r, r-l+1)

        return s[reslen[0]:reslen[1]+1]
        
