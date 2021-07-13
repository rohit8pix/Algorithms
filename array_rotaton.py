def arerotation(string1, string2):
	s1 = len(string1)
	s2= len(string2)
	temp = ''
	if s1!=s2:
		return 0
	temp = string1+string2
	if (temp.count(string2)>0): # check if string2 is subset of temp 
		return 1 
	else:
		return 0
