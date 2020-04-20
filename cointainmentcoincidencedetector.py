

def main_process(table_list, bound, cb = 5):
    coincidences = []

    for sequences in table_list:
        for new_sequences in table_list:

            coFlag = True
            count = 0
            for elements in sequences['table'].keys():




                if int(elements) <= int(new_sequences['maximum']): #so we are not OFF the sequence
                    count += 1
                    if not (elements in new_sequences['table'].keys()):

                        coFlag = False
                        break




            if coFlag:

                if sequences['name'] != new_sequences['name'] and count >= cb:
                    coincidences.append((sequences['name'], new_sequences['name']))

            if len(coincidences) > bound:
                break

        if len(coincidences) > bound:
            break

    return coincidences


if __name__ == '__main__':

    f = open('intSequenceTableList', 'r')
    table_list =  eval(f.read())

    f.close()


    bound = 1000

    coincidencelist = main_process(table_list, bound, 10)

    f = open('containmentcoincidencelist', 'w')
    f.write(str(coincidencelist))
    f.close()
    #print(coincidencelist)
