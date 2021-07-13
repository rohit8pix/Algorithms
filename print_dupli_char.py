'''method1'''
def dupli(arr):
	duplicates = []
	for char in arr:
		if arr.count(char)>1:
			if char not in duplicates:
				duplicates.append(char)
        
        
'''method2'''
def dupli_dictionary(arr):
	duplicates={}
	for char in arr:
		if char in duplicates:
			duplicates[char]+=1
		else:
			duplicates[char]=1
	for key, value in duplicates.item():
		if value>1:
			print(key)
	print()
