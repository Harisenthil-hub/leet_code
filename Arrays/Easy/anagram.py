a = 'hello'
b = 'hlelo'



def anagram(s,t):
    
    count1 = {}
    count2 = {}
    
    if len(s) != len(t):
        return False
            

    for i in a:
        if i not in count1:
            count1[i] = 1
        else:
            count1[i] += 1
            
    for i in b:
        if i not in count2:
            count2[i] = 1
        else:
            count2[i] += 1

    for j in count1:
        if j not in count2 or count1[j] != count2[j]:
            return False
    return True
        
    
    
print(anagram(a,b))
