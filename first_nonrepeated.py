def nonrepeat(arr):
	# no of chars = 256
	def getcharcount(arr):
		count = [0]*256
		for i in arr:
			count[ord(i)]+=1
		return count 

	def first(arr):
		count = getcharcount(arr)
		index = -1
		k=0

		for i in arr:
			if count[ord(i)]==1:
				index = k
				break
			k+=1
		return index

	index = first(arr)
	return index
