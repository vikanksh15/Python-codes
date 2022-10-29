def missing(arr1,arr2):
    arr1.sort()
    arr2.sort()
    # for num1,num2 in zip(arr1,arr2):
    #     if num1 != num2:
    #         return num1
    # return num1[-1]

    # count = {}
    
    # for num2 in arr2:
    #     if num2 in count:
    #         count[num2]+=1
    #     else:
    #         count[num2]=1
    
    # for num1 in arr1:
    #     if num1 in count:
    #         count[num1]-=1
    #     else:
    #         count[num1]=1
            
    # for k in count:
    #     if count[k]!=0:
    #         return k
    

    # diff = sum(arr1)-sum(arr2)
    # return diff   #problematic approach i.e. if the numbers are too large 
                #we could end up getting a overflow 
                #or if numbers are very small and have ton of deciaml places
                #then we might lose some information 

    #clever trick approach - XOR
    
    l = 0
    for num1,num2 in zip(arr1,arr2):
        l = num1^num2
        if l != 0:
            return num1
    return num1[-1]
    
    
r = missing([1,2,3,1,4,5,6,7],[7,1,4,2,6,3,1])
print(r)