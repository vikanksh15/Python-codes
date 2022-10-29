def pairsum(arr,k):
    if len(arr)<2:
        print("Error no element found to pair")
    
    # #sets for tracking
    # seen = set()
    # output = set()

    # #for every number in array( O(n) complexity: Single linear search)
    # for num in arr:
    #     #sets target difference in arrayx ()
    #     target = k-num

    #     if target not in seen: #check whether the corresponding number to form a pair in the set (Insert and find operations of a set are both average O(1))
    #         seen.add(num)
    #     else:
    #         output.add(( (min(num,target)),max(num,target)))
    
    # # return len(output)
    # print('\n'.join(map(str,list(output))))
    prevMap = {}
    for n,i in enumerate(arr):
        if k-i in prevMap:
            print(f"({k-i},{i})")
        prevMap[n]=i


pairsum([1,3,2,1,4,5],5)