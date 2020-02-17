
#Given two lists of integers
#This systematically checks if each element of the first list can be expressed as sum of elements in the second list
def IsListExpressed(List1, List2):
    weight = 1

    i = 0
    while i < min(len(List1), weight):
        if not isSubsetSum(List2[:weight+1], min(len(List2), weight), List1[i]): #we truncate List2 with the weight
            return False
        i+=1

    return True


def isSubsetSum(tset,index, tsum):
    # Base Cases
    if (tsum == 0) :
        return True
    if (index == 0 and tsum != 0) :
        return False

    # If last element is greater than
    # sum, then ignore it
    if (tset[index - 1] > tsum) :
        return isSubsetSum(tset, index - 1, tsum);

    # else, check if sum can be obtained
    # by any of the following
    # (a) including the last element
    # (b) excluding the last element
    return isSubsetSum(tset, index-1, tsum) or isSubsetSum(tset, index-1, tsum-tset[index-1])


if __name__ == '__main__':
    print("the main!")
