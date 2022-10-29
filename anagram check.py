# def anagram(a,b):
#     a = a.replace(" ","").lower()
#     b = b.replace(" ","").lower()

#     return sorted(a)==sorted(b)

#Anagram = Pharase formed by rearranging the letters of diffferent word or phrase typically using the same letters
#Example : act = cat, dusty = study, below = elbow , bad credit = debit card
def anagram(a,b):
    a = a.replace(' ','').lower() #removing the space and converting all characters into lower case
    b = b.replace(' ','').lower() #removing the space and converting all characters into lower case
    if len(a) != len(b):  #if length of both string are not same then given string isn't anagram
        return False
    
    count = {}  #creating hashmap to count frequency of letters
    
    for letter in a: ##counting the frequency of letters in string A
        if letter in count:
            count[letter]+=1
        else:
            count[letter] = 1

    for letter in b: ##cross-check for same letter and deleting frequency 
        if letter in count:
            count[letter]-=1
        else:
            count[letter] = 1
    
    for k in count:  ##check if frequency of all letters is zero then given string is anagram
        if count[k] != 0:
            return False
        else:
            return True




result = anagram('bad credit','debit card')
print(result)