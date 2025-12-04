def isValid(s: str) -> bool:
        if s[0] not in '[({':
            return False 
        stack = []
        hsh = {']':'[','}':'{',')':'('}
        for i in s:
            print(stack)
            if i in '({[':
                stack.append(i)
            elif stack and hsh[i] == stack[-1]:
                    stack.pop()
        if stack:
            return False
        else:
            return True
        
print(isValid('(])'))