def compress(s):
    r = ""
    l = len(s)
    if l==0:
        return 0
    if l==1:
        return s+"1"

    count = 1
    i=1
    while i < l:
        if s[i]==s[i-1]:
            count+=1
        else:
            r = r + s[i-1] + str(count)
            count = 1
        i+=1
    
    r = r + s[i-1]+str(count)

    return r

a = compress("aaBBCCCDDD")
print(a)