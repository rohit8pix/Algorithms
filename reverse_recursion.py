def reverse(string):
	if len(string)==0:
		return
	temp = string[0]
	reverse(string[1:])
	print(temp)

reverse("rohit")


def rev_usingstack(string):
	stack =[]
	for i in range(len(string)):
		stack.append(string[i])
	for i in range(len(string)):
		string[i]=stack.pop()


str = list("geeks")
rev_usingstack(str)
str = "".join(str)
print(str)
