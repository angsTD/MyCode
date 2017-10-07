def swapIndex(stringList,indA, indB):
	temp = stringList[indA]
	stringList[indA] = stringList[indB]
	stringList[indB] = temp

def permute(cList,stInd,endInd):
	if(stInd==endInd):
		str1 = ''.join(cList) #convert character list into string before printing
		print str1
	else:			
		for ind in range(stInd,endInd+1):
			swapIndex(cList,stInd,ind)
			permute(cList,stInd+1,endInd)
			swapIndex(cList,stInd,ind) #restore the original string before swapping the subsequent indices and then permuting

charString = "abcd"
charList = list(charString) #string is immutable in python, convert it into list
permute(charList,0,len(charList)-1)


