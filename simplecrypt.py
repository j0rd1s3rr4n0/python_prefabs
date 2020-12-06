filename = "save.txt"
elements = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ','\n']
replacin = ['/Ä01','/Ä02','/Ä03','/Ä04','/Ä05','/Ä06','/Ä07','/Ä08','/Ä09','/Ä10','/Ä11','/Ä12','/Ä13','/Ä14','/Ä15','/Ä16','/Ä17','/Ä18','/Ä29','/Ä20','/Ä21','/Ä22','/Ä23','/Ä24','/Ä25','/Ä26','+/Ä27+','/Ä28']
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
