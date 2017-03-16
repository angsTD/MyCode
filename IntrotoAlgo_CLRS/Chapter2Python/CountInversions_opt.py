import time

def printArray( unsortedList ):
	if(len(unsortedList)!= 0):
	    for index in range(0,len(unsortedList)):
	        print "A[%d] = %d " %(index,unsortedList[index])

def CountInterSubarrayInversions(sortedSmall,mergedArray,lsInd,leInd,rsInd,reInd):

	inversionCount = 0

	lenA = leInd-lsInd+1
	lenB = reInd-rsInd+1
	indexA = lsInd
	indexB = rsInd
	index = 0
	while (indexA < (lsInd+lenA) and indexB < (rsInd+lenB)):
		if(sortedSmall[indexB]>=sortedSmall[indexA]):
			mergedArray.append(sortedSmall[indexA])
			indexA += 1
		else:
			mergedArray.append(sortedSmall[indexB])
			indexB += 1
			inversionCount += ((lsInd+lenA)-indexA)
	mergedArray += sortedSmall[indexA:(leInd+1)]
	mergedArray += sortedSmall[indexB:(reInd+1)]

	return inversionCount

def CountSubarrayInversions(unsortedA,startInd,endInd):
	listM = []
	lenA = endInd-startInd+1
	leftAinvCount = 0
	rightAinvCount = 0
	interAinvCount = 0
	if(lenA > 1):
		n = (endInd-startInd+1)/2
		leftAinvCount = CountSubarrayInversions(unsortedA,startInd,startInd+n-1)
		rightAinvCount = CountSubarrayInversions(unsortedA,startInd+n,endInd)
		interAinvCount = CountInterSubarrayInversions(unsortedA,listM,startInd,startInd+n-1,startInd+n,endInd)
		unsortedA[startInd:(endInd+1)] = listM[0:(endInd+1-startInd)]
	return (leftAinvCount+rightAinvCount+interAinvCount)

testArrayList = [3,24,23,2,5,-2,-19,4,17,-6,34,22,23,-54,47,42,8724,24894,474,4284,5442,4824,-2424,-4284]
testArrayList2 = [8,7,6,5,4,3,2,1]
testArrayList3 = [8,7,5,5,5,5,5,5]
recPath = []

fp = open("InversionsTestCase.txt")
lines = map(int,fp.readlines())
print "length of lines %d" %len(lines)
start_time = time.clock()
invCount = CountSubarrayInversions(lines,0,len(lines)-1)
print("--- %s seconds ---" % (time.clock() - start_time))
print " Inversion Count %d \n" %invCount
#printArray(lines)
