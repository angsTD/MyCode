

def findelement(stInd,endInd,unimodArr):
	maxElement = 0
	midind = (stInd + endInd)/2
	if(unimodArr[midind-1]<unimodArr[midind] and unimodArr[midind]>unimodArr[midind+1]):
		return unimodArr[midind]
	elif (unimodArr[midind-1]<unimodArr[midind]):
		return findelement(midind,endInd,unimodArr)
	else:
		return findelement(stInd,midind,unimodArr)


testArray = [1,2,3,4,5,6,7,8,9,10,11,10,4,3]

print "Max Element: %d" %findelement(0,(len(testArray)-1),testArray)
