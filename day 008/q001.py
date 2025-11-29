def myAtoi( s: str) -> int:
    if not s or s == "-" or s == '+':
        return 0
    res = ''
    for i in s:
        if i ==" " and not res:
            continue
        if '0' <= i <='9' or (not res and ( i=='-' or i == '+')):
            res += i

        elif res :
            break
        
        else:
            return 0
    try:
        res = int(res)
    except Exception:
        return 0
    min1 = -2**31
    max1 = -min1 -1
    if res < min1:
        return min1
    elif res > max1:
        return max1 

    return res
        

s = "     -111 121 fm,d," 

print(myAtoi(s))
