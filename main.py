def removeEvens(k):
    newlist = k 
    numPopped = 0
    for i in range (0, len(k)):
       if newlist[i - numPopped] % 2 == 0 and newlist[i - numPopped] != 0:
           newlist.pop(i - numPopped)
           numPopped = numPopped + 1 

    return newlist

print(removeEvens([1, 2, 3, 4, 5, 6, 7, 8, 9,]))
    
