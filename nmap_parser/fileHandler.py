''' This module deals with the file operations. The operations like read, write , append are done in this module. '''

#cfg_data = None

def fileWrite(data, flag=0):
	''' The function writes the data to the result.txt file. The data will be the depricated APIs, new APIs between the text cycles.
		data :- First argument is data to be writen to the file 
		flag :- Flag indicating if the data is depricated APIs, new APIs or common APIs.
		'''
	fp = open('result.txt', 'a')
	fp.write(data)
	fp.close()

def fileRead(path):
	''' Function reads the file content. The contents are returned as string. 
		path :- Takes path of the file as argument '''
	try:	
		fp = open(path, 'r')
		
	except IOError:
		print ("Error opening the file %s",  path)
		return None
		
	with fp:
		robj = fp.read()
		fp.close()
		return robj
		
if __name__ == "__main__":
	print('File handling module')
	
