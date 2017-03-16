def printArray( unsortedList ):
	if(len(unsortedList)!= 0):
	    for index in range(0,len(unsortedList)):
	        print "A[%d] = %d " %(index,unsortedList[index])

def printRecPath( pathList ):
    #for index in range(0,len(pathList)):
    if(len(pathList)!=0):
	    index = len(pathList) - 1;
	    print "level: %d, branch %d " %(index+1,pathList[index])

def Merge(sortedSmallA,sortedSmallB,mergedArray):
	#print "Array 1 Before Merge"
	#printArray(sortedSmallA)
	#print "Array 2 Before Merge"
	#printArray(sortedSmallB)

	lenA = len(sortedSmallA)
	lenB = len(sortedSmallB)
	indexA = 0
	indexB = 0
	for index in range(0,len(sortedSmallB)+len(sortedSmallA)):
		#print "index of A: %d, len A: %d , index of B: %d, len B: %d Main Index %d" %(indexA, lenA, indexB, lenB, index)
		if(indexB == lenB and indexA!= lenA):
			mergedArray.append(sortedSmallA[indexA])
			indexA += 1
		if(indexA == lenA and indexB!= lenB):
			mergedArray.append(sortedSmallB[indexB])
			indexB += 1
		if(indexB != lenB and indexA != lenA):
			if(sortedSmallB[indexB]>=sortedSmallA[indexA]):
				mergedArray.append(sortedSmallA[indexA])
				indexA += 1
			else:
				mergedArray.append(sortedSmallB[indexB])
				indexB += 1
	#print "Array After Merge"
	#printArray(mergedArray)

def MergeSort(unsortedA, recursionPath):
	listA = []
	listB = []
	listM = []
	lenA = len(unsortedA)
#	print "length of unsorted Array %d" %lenA 
#	print "recursion path"
	printRecPath(recursionPath)
	if(lenA > 1):
		n = lenA/2
#		print "Halved length n %d " %n
		for index in range(0,n):
			listA.append(unsortedA[index])
		for index in range(n,lenA):
			listB.append(unsortedA[index])
		recursionPath.append(0)
		MergeSort(listA,recursionPath)
		recursionPath.pop()
		recursionPath.append(1)
		MergeSort(listB,recursionPath)
		recursionPath.pop()
		Merge(listA,listB,listM)
#		print " Array After Merge 2"
		for ind in range(0,len(unsortedA)):
			unsortedA[ind] = listM[ind]
#		printArray(unsortedA)
	else:
		unsortedA = unsortedA

testArrayList = [3,24,23,2,5,-2,-19,4,17,-6,34,22,23,-54,47,42,8724,24894,474,4284,5442,4824,-2424,-4284]
testArrayList2 = [4,3]
recPath = []
MergeSort(testArrayList,recPath)
print " \nFinal Merged Array"
printArray(testArrayList)
