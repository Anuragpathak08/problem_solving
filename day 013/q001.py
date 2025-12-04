def isValid(s: str) -> bool:
        if s[0] not in '[({':
            return False 
        stack = []
        hsh = {']':'[','}':'{',')':'('}
        for i in s:
            if stack and hsh.get(i) == stack[-1]:
                stack.pop()
                continue
            stack.append(i)
        if stack:
            return False
        else:
            return True
        
print(isValid('(])'))