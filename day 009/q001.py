# leetcode 10
def isMatch(self, s: str, p: str) -> bool:
        import re
        try :
            a = re.match(p,s).group()
        except:
            return False
        
        if s == a :
            return True 
        else :
            return False 