def unique_char(s):
    return len(set(s))==len(s)

def uni_char2(s):
    c = set()
    for char in s:
        if char in c:
            return False
        else:
            c.add(char)
    return True 

mystring = uni_char2("abcde")
print(mystring)
