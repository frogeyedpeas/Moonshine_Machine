

#given the int sequence and (in the future) a coincidence library, we can search for certian classes of coincidences
#for now we are attempting to search for greedy packing coincidences
#we can add a bound condition, to define what we consider to be "small" linear combinations
#if something isn't small then it is invalid

def pack_num(target_num, array, bound=10):

    if target_num == 0: #edge case, empty sums are always summable
        return []

    #we need to find the smallest index the array that is strictly bigger than target_num
    i = 0
    while i < len(array) and array[i] <= target_num:
            i+=1

    if i == 0: #we failed the condition 
        return None

    i-=1 #either we went of the array or array[i] is TOO big, so in either case we decrement 

    phase = (target_num//array[i])

    if phase > bound:
        return None

    reduced_target = target_num - array[i]*phase
    

    sub_value = pack_num(reduced_target, array)
    
    if sub_value != None:
        return [(phase, i)] + sub_value 
    
    return None


#this is condition for checking which things can be packed 
def can_be_packed(first_array, second_array, bound, pack_bound = 10):

    i = 0
    while i < bound and i < len(first_array):

        if pack_num(first_array[i], second_array) == None:
            return False

        i+=1

    return True

#driver code
if __name__ == '__main__':

    f = open('intSequenceList', 'r')

    intarray = eval(f.read())

    f.close()


    g = open('coincidences_detected', 'w')
    
    positive_hits = []

    i = 0
    while i < len(intarray):

        j = i +1

        while j < len(intarray):

            print(i, j) 
            if can_be_packed(intarray[i],intarray[j], 5):
                g.write(str((i,j))+'\n')              
                positive_hits.append((i,j))

            j+=1

        i+=1



    g.close()




