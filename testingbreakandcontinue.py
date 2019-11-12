

i = 0
j = 0
while i < 5:
    flag = False
    print(i,j)
    if i==2 and j ==2:
        print("the code worked")
    j = 0
    while j < 5:
        if i==2 and j==2:
            print("made the condition")
            flag = True
            break
        j+=1

    if flag:
        continue
    i+=1
