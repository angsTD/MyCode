#Define Insertion Sort method
import time
def InsertionSort( unsortedList ):
	for index in range(1,len(unsortedList)):
		for ind in range(0,index):
			if unsortedList[index] < unsortedList[ind]:
				temp = unsortedList[index]				
				innerLoopIndex = index
				while (innerLoopIndex > ind):
					unsortedList[innerLoopIndex] = unsortedList[innerLoopIndex-1]
					innerLoopIndex -= 1
				unsortedList[ind] = temp


def printList(unsortedList):
	print "Array Length is %d" %len(unsortedList)
	for index in range(0,len(unsortedList)):
		print "array[%d] = %d" %(index,unsortedList[index])



fp = open("InversionsTestCase.txt")
#lines = fp.readlines()
lines = map(int,fp.readlines())
testArray1 = [3,24,23,2,5,-2,-19,4,17,-6,34,22,23,-54,47,42,8724,24894,474,4284,5442,4824,-2424,-4284]


start_time = time.time()
InsertionSort( lines )

print("--- %s seconds ---" % (time.time() - start_time))

#printList( lines )

				