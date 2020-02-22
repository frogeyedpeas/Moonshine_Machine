

#given the int sequence and (in the future) a coincidence library, we can search for certian classes of coincidences
#for now we are attempting to search for greedy packing coincidences

def pack_num(target_num, array):

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
    reduced_target = target_num - array[i]*phase
    
    print(reduced_target)

    sub_value = pack_num(reduced_target, array)
    
    if sub_value != None:
        return [(phase, i)] + sub_value 
    
    return None


#this is condition for checking which things can be packed 
def can_be_packed(first_array, second_array, bound):

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


    positive_hits = []

    i = 0
    while i < len(intarray):

        j = i +1

        while j < len(intarray):

            if can_be_packed(first_array, second_array, 5):
                
                positive_hits.append((i,j))

            j+=1

        i+=1

    g = open('coincidences_detected', 'r')

    g.write(str(positive_hits))

    g.close()




