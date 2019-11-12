
from moonshineutils import IsListExpressed
from collections import defaultdict
import pickle
import cProfile



def pre_processor():
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



	StatusTable = defaultdict(lambda: [])


	print("alright baby")
	IntAggregator = []
	count = 0
	for elements in mod:
		element_split = elements.split(' ', 1)
		if len(element_split) == 1:
			continue

		Name  = element_split[0]
		IntArray  = element_split[1].split(',')[1:-1]

		i = 0
		while i < len(IntArray):
			IntArray[i] = int(IntArray[i]) #converting an individual line to a collection of integer


			i+=1
		IntAggregator.append(IntArray)

	#f = open('IntAggregator', 'wb')
	#pickle.dump(IntAggregator, f)
	#f.close()
	#print("pickled for tomorrow!")

	f = open('sequenceFile.txt', 'w')
	for sequences in IntAggregator:
		for elements in sequences:
			f.write(str(elements)+' ')
		f.write('\n')
	f.close()
	return IntAggregator



pre_processor()
#For each pair of lines L1, L2 in IntAggregator, we want to see if there is a way to write each element of L1 as a (potentially empty) sum of elements of L2
#Any such pair that is detected is a potential collision worth exploring

#So we have an index i = 0, which runs to len - 1, and index j = i+1 which runs ot element
#if either L_i or L_k contain negative numbers then they are automatically discluded [Should we insist that things are in ascending order?]


#IntAggregator = pre_processor()
#f = open('IntAggregator', 'rb')
#IntAggregator = pickle.load(f)
#f.close()

def AggregatorProcessor(IntAggregator):
	PotentialHits = []
	MinListLength = 5
	MinGap = 5
	i=0
	while i < len(IntAggregator)-1:

		#check for validity of i-column

		#print(i)
		phase = 0
		prev = 0
		while phase < len(IntAggregator[i]) and i < len(IntAggregator) - 1:
			#right now we enforce at least 10 elements in the i-list to filter some results
			if len(IntAggregator[i]) < MinListLength:
				i+=1
				phase = 0
				prev = 0
				continue

			if IntAggregator[i][phase] < 0:
				i+=1
				phase = 0
				prev = 0
				continue

			#print(IntAggregator[i][phase])
			if IntAggregator[i][phase] <= prev+MinGap:
				i+=1
				phase = 0
				prev = 0
				continue

			prev = IntAggregator[i][phase]
			phase+=1

		#now assuming that i-column is valid
		#we search for a potentially valid j-column
		j = i+1
		while j < len(IntAggregator):
			#print(i,j)

			phase = 0
			prev = 0
			while j < len(IntAggregator) and phase < len(IntAggregator[j]):

				if len(IntAggregator[j]) < MinListLength:
					j+=1
					phase = 0
					prev = 0
					continue

				if IntAggregator[j][phase] < 0:
					j+=1
					phase = 0
					prev = 0
					continue

				if IntAggregator[j][phase] <= prev+MinGap: #adding +1 blocks natural numbers
					j+=1
					phase = 0
					prev = 0
					continue

				prev = IntAggregator[j][phase]
				phase+=1

			#now we have a valid i and j column we can search for subset sum type collisions

			#print("processing a new pair")
			if j < len(IntAggregator) and i < len(IntAggregator) -1:
				if IsListExpressed(IntAggregator[i], IntAggregator[j]): #deleted [:10] strip
					#print("FOUND A POTENTIAL MATCH SEE BELOW: ")
					#print(IntAggregator[i])
					#print(IntAggregator[j])
					PotentialHits.append([IntAggregator[i], IntAggregator[j]])

				if IsListExpressed(IntAggregator[j], IntAggregator[i]): #deleted [:10] strip
					#print("FOUND A POTENTIAL MATCH SEE BELOW: ")
					#print(IntAggregator[j])
					#print(IntAggregator[i])
					PotentialHits.append([IntAggregator[j], IntAggregator[i]])

			j+=1
		i+=1

	return PotentialHits


#cProfile.run("AggregatorProcessor(IntAggregator)")



#print(IntAggregator)
