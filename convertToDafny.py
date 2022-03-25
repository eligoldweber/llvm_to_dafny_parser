#!/usr/bin/python


import sys, getopt


def findSize(s):
	s = s.replace(',',"")
	if(s == 'i8'):
		return 1
	if(s == 'i16'):
		return 2
	if(s == 'i32'):
		return 4
	if(s == 'i64'):
		return 8
	else:
		return -1
		
def handleArg(arg,size):
	if (len(arg) <= 0):
		return
	arg = arg.replace(',',"")
	if(arg[0] == '%'):
		return arg
	else:
		# print(int(arg))
		# arg = arg.replace(',',"")
		convertedArg = "D(Int("+arg+",IntType("+str(size)+",false)))"
		# print(convertedArg)
		return convertedArg
		
		
		
def parseLLVM(in_filename,out_filename):
	fo = open(in_filename,"r+")
	fout = open(out_filename,"w+")
	llvmCode = fo.readlines()
	count = 0
	insList = []
	for line in llvmCode:
		print("Line{}: {}".format(count,line.strip()))
		count = count + 1
		parsedList = []
		args = line.split()
		# print (args)
		if(len(args)> 0):
			if(args[0][-1] == ':'): #this is a block name
				parsedList = []
				insList = []
				fout.write("var " + args[0][0:-1] + " = ")
				continue
			
			if(args[0][0] == '%'):
				dst = args[0]
				ins = args[2]
				# writeToOut(ins)
				parsedList.append(ins)
				parsedList.append(dst)
			
				if(ins == 'add'):
					size = findSize(args[4])
					parsedList.append(str(size))
					arg1 = args[5].replace(',',"")
					arg2 = args[6].replace(',',"")
				
					arg1 = handleArg(arg1,size)
					arg2 = handleArg(arg2,size)
					parsedList.append(arg1)
					parsedList.append(arg2)
				
				if(ins == 'icmp'):
					comp = args[3]
					size = findSize(args[4])
					arg1 = args[5].replace(',',"")
					arg2 = args[6].replace(',',"")
				
					arg1 = handleArg(arg1,size)
					arg2 = handleArg(arg2,size)
					parsedList.append(comp)
					parsedList.append(str(size))
					parsedList.append(arg1)
					parsedList.append(arg2)
			
				if(ins == 'load'):
					# print(args)
					size = findSize(args[3])
					src = args[5].replace(',',"")
					src = handleArg(src,size)
					parsedList.append(str(size))
					parsedList.append(src)
			
			
				
			if(args[0] == 'store'):
				arg1Size = findSize(args[1])
				arg1 = handleArg(args[2],arg1Size)
				parsedList.append(args[0])
				parsedList.append(arg1)
				arg2 = handleArg(args[4],arg1Size)
				parsedList.append(arg2)
			
			if(args[0] == "br"):
				# print(args)
				parsedList.append(args[0])
				arg1 = args[2].replace(',',"")
				if(len(args) > 3):
					argT = args[4].replace(',',"")
					argF = args[6].replace(',',"")
					parsedList.append(arg1)
					parsedList.append(argT)
					parsedList.append(argF)
				
			if(args[0] == 'ret'):
				# arg1Size = findSize(args[1])
				# arg1 = handleArg(args[1],arg1Size)
				parsedList.append(args[0])
				parsedList.append(args[1])
		
				
		
			if(len(parsedList) > 0):
				insList.append(formatIns(parsedList))
			
		# print (insList)
		else:
			fout.write(createLLVMBlock(insList))
	# Close opend file
	fo.close()
	fout.close()
	

def createLLVMBlock(listOfIns):
	block = "Block(["
	for ins in listOfIns[:len(listOfIns)-1]:
		block = block + str(ins) + ",\n"
	block = block + listOfIns[len(listOfIns)-1] + "];\n\n"
	return block
	
def formatIns(ins):
	insStart = "INS("
	insStart = insStart+ins[0].upper()+"("
	for item in ins[1:len(ins)-1]:
		insStart = insStart + item + ","
	insStart = insStart + ins[len(ins)-1] + "))"
	return insStart

def writeToOut(ins,f):
	insStart = "INS("
	f.write(insStart+ins[0].upper()+"(")
	for item in ins[1:len(ins)-1]:
		f.write(item + ",")
	f.write(ins[len(ins)-1])
	f.write("))\n")
	
# def cleanInputFile(in_filename):
# 	fo = open(in_filename,"r+")
# 	fout = open("teset.ll","w+")
# 	llvmCode = fo.readlines()
# 	for line in llvmCode:
# 		print("Line: {}".format(line.strip()))
# 		args = line.split();
# 		for word in args:
# 			print (word)
#
# 	fo.close()
# 	fout.close()
	
def main(argv):
   inputfile = ''
   outputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
   except getopt.GetoptError:
      print('test.py -i <inputfile> -o <outputfile>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print('test.py -i <inputfile> -o <outputfile>')
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg
   print('Input file is "', inputfile)
   print('Output file is "', outputfile)
   # cleanInputFile(inputfile)
   parseLLVM(inputfile,outputfile)


if __name__ == "__main__":
   main(sys.argv[1:])
	 
	 
print("DONE")

#######


	
	
	
	
	
	
	