#solution 1
s = "PAYPALISHIRING"

def convert (s,numrow):
    str1 = ['' for i in range(numrow)]
    i=0
    l = len(s)
    while i < l:
        j = 0
        while j<numrow and i<l :
            str1[j]+=s[i]
            i+=1
            j+=1

        k  =numrow -1
        while k>1 and i<l:
            str1[k-1]+=s[i] 
            i+=1  
            k-=1  

    s = "".join(str1) 
    
    return s

print(convert(s,3))

# solution 2 (3ms Beats 98.99%)


s = "PAYPALISHIRING"

def convert (s,numRows):
    if numRows == 0 :
        return s
    str1 = ['']*numRows
    cur=0

    for i in s:
        str1[cur] += i 
        if cur  == 0:
            step = 1
        elif cur == numRows-1:
            step = -1
        cur +=step

    s = "".join(str1) 
    
    return s

print(convert(s,len(s)))

