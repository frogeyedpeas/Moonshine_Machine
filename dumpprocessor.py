class Sequence_Table:

    def __init__(self, name,maximum, table=None):
        if table==None:
            self.table = {}
        else:
            self.table = table
        self.name = name
        self.maximum = maximum

    def __str__(self):
        return str({'table': self.table, 'name': self.name, 'maximum': self.maximum})
    def __repr__(self):
        return self.__str__()

if __name__ == '__main__':

    test = '''
    x = Sequence_Table('hi', 10, {'hello':{}})
    print(x)

    with open('trash.txt', 'w') as trash:
        trash.write(str([x]))
    '''


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

            line_split = nextLine.split() #this grabs just the integer sequence part

            split_line = line_split[1]
            line_name = line_split[0]


            int_string_sequence = split_line.split(',')[1:-1] #we remove the trailing and leading elements to just preserve the actual integer sequence

            rejectFlag = False
            i = 1
            next_Table = Sequence_Table(line_name,0)
            next_Table.table[int_string_sequence[0]] = True
            while i < len(int_string_sequence):

                next_Table.table[int_string_sequence[i]] = True

                if int_string_sequence[i] < int_string_sequence[i-1]:
                    rejectFlag = True
                    break

                i+=1

            if not rejectFlag:
                new_max = int_string_sequence[i-1]

                if int(new_max) >= 1000:
                    next_Table.maximum = int_string_sequence[i-1]
                    sequenceList.append(next_Table)

            nextLine = f.readline()
            print(nextLine) # this is for debugging comment out once we prove feasibility


        #sequenceList has been built so we need to save it now
        #we considered pickling it but its probably easier to just save it with as a file for writing

        with open('intSequenceTableList', 'w') as g:
            g.write(str(sequenceList))
