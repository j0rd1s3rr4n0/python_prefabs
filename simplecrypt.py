count = 0
filename = "save.txt"
elements = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','']
replacin = ['_','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for element in elements:
	char1 = elements[count]
	char2 = replacin[count]
	filer = open(filename, "r")
	filew = open(filename, "r+")	
	buff = filer.read()
	rbuff = buff.replace(char1, char2)
	filew.write(rbuff)
	filer.close()
	filew.close()
	count+=1
