


f = open('stripped', 'r')
x = f.read()
f.close()

x = x.split('\n')
mod = x[4:] #this array now only consists of sequences 

#we will now go through element in mod, trim off the name, then split it, then for coefficients that are very large 
#we will durmp them into a hashtable, and link the names, and then see how many "coincidences" are left


print(len(mod))

wrap = mod[0].split(' ', 1)
print(wrap)
wrap[1] = wrap[1].split(',')
wrap[1] = wrap[1][1:len(wrap[1])-1]

print(wrap[1])


from collections import defaultdict


StatusTable = defaultdict(lambda: [])


print("alright baby")
for elements in mod:
	element_split = elements.split(' ', 1) 
	Name  = element_split[0]
	IntArray  = element_split[1].split(',')[1:-1] 
	i = 0
	while i < len(IntArray):
		IntArray[i] = int(IntArray[i])
		if IntArray[i] > 100000:
			StatusTable[IntArray[i]] += [Name]
			StatusTable[IntArray[i]+1] += [Name]
			StatusTable[IntArray[i]-1] += [Name]

			if len(StatusTable[IntArray[i]]) >= 2:
				print('DETECTED COINCIDENCE ', StatusTable[IntArray[i]], IntArray[i])

			if len(StatusTable[IntArray[i]+1]) >= 2:
				print('Is Jeremy even a bot? ', StatusTable[IntArray[i]+1], IntArray[i] +1)


			if len(StatusTable[IntArray[i]-1]) >= 2:
				print('DETECTED COINCIDENCE ', StatusTable[IntArray[i]-1], IntArray[i] -1)
	

		i+=1
	
print(mod[0])

print(x[5])
