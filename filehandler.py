import os, re, sys, getopt
from File import File
from Node import Node


PATH = os.path.dirname(os.path.abspath(__file__))
INPUT_PATH = PATH + "/data-input/"
OUTPUT_PATH = PATH + "/data-output/"

def parse(argv):
	inputFileName = "" 
	nodeFileName  = ""
	outputFileName =""
	try:
		opts, args = getopt.getopt(argv, "hf:n:o:", ["ffile=", "nfile=", "ofile="])
		if len(argv)> 6 and '-h' not in argv:
			print("Error: Too many arguments")
			sys.exit(2)
	except getopt.GetoptError:
		print('solution.py -f <inputFile> -n <inputNode> -o <outputFile> -h ')
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print('solution.py -f <inputFile> -n <inputNode> -o <outputFile> -h ')
			sys.exit()
		elif opt in ("-f", "--ffile"):
			inputFileName = arg
		elif opt in ("-n","--nfile"):
			nodeFileName = arg
		elif opt in ("-o", "--ofile"):
			outputFileName = arg
		
	if inputFileName == '' and nodeFileName == '':
		print("Error: <inputFile> and <inputNode> missing ")
		sys.exit()
	elif inputFileName == '':
		print("Error: <inputFile> missing ")
		sys.exit()
	elif nodeFileName == '' or nodeFileName == '-o':
		print("Error: <inputNode> missing ")
		sys.exit()
	return [inputFileName, nodeFileName,outputFileName]


def buildArrays(filename,nodename):
	try:
		fileArray = []
		nodeArray = []
		#build file array
		with open(INPUT_PATH + filename, 'r') as rf1:
			#to avoid memory issues with large files, read input per line
			for line in rf1:
				line = line.strip()
				# check if line is empty or contains a #
				if line:
					if(line.startswith('#')):
						continue
					#data of interest could be file or node
					file_info = line.split(" ")
					fileInstance = File(file_info[0], file_info[1]) 
					fileArray.append(fileInstance)
	   #build node array
		with open(INPUT_PATH + nodename, 'r') as rf2:
			#to avoid memory issues with large files, read input per line
			for line in rf2:
				line = line.strip()
				# check if line is empty or contains a #
				if line:
					if(line.startswith('#')):
						continue
					#data of interest could be file or node
					file_info = line.split(" ")
					nodeInstance = Node(file_info[0], file_info[1]) 
					nodeArray.append(nodeInstance)
				#returns tuple of filearry and node array
			return (fileArray,nodeArray)
	except:
		print("Error: Rows of input file should be of the format <filename> <filesize>")
		sys.exit()


def output(inFileArray,outputFileName):

	for f in inFileArray:
		if(f.location == "unknown"):
			f.location = "NULL"

	if outputFileName == "":
		for f in inFileArray:
			print(f.name + " " + f.location)
	else:
		try:
			with open(OUTPUT_PATH + outputFileName, 'w') as outFile:
				for f in inFileArray:
					outFile.write(f.name + " " + f.location + "\n")
		except:
			print("Error: Unable to write to file <" + outputFileName + ">")


