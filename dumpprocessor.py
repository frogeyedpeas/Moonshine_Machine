
growtharray = [1,2,4,8,16,32,64,128]
growthlength = 7

with open('datadump', 'r') as f:

    sequenceList = [] 

    # need to skip the preamble in the file by reading 4 lines 

    txt1 = f.readline()
    txt1 = f.readline()
    txt1 = f.readline()
    txt1 = f.readline()

    #now we are at the first of many sequences

    nextLine = f.readline()
    while nextLine != '':
    
        split_line = nextLine.split()[1] #this grabs just the integer sequence part
        int_string_sequence = split_line.split(',')[1:-1] #we remove the trailing and leading elements to just preserve the actual integer sequence
        
        rejectFlag = False
        i = 0
        while i < len(int_string_sequence):
            int_string_sequence[i] = int(int_string_sequence[i])

            if i <= growthlength:
                if int_string_sequence[i] < growtharray[i]:
                    rejectFlag = True
            i+=1

        if not rejectFlag:
            sequenceList.append(int_string_sequence)
        
        nextLine = f.readline()
        print(nextLine) # this is for debugging comment out once we prove feasibility


    #sequenceList has been built so we need to save it now 
    #we considered pickling it but its probably easier to just save it with as a file for writing 

    with open('intSequenceList', 'w') as g:
        g.write(str(sequenceList))


