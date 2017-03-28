from __future__ import print_function
  
'''
			===========================================
			Program for file Distributuion across nodes
			===========================================
Given a list of files with their sizes and a list of compute nodes with their available space, write a
program that produces a distribution plan of how to place the files on the nodes. The plan should make
the total amount of data distributed to each node as balanced as reasonably possible. Note that this is
different from balancing the amount of available space remaining on each node after the distribution
						================
						Solution Summary
						================
* Input files are parsed by file named filehandler.py
* Files and nodes initialized as objects for easy manipulation(File.py & Node.py)
* Prepare input for distribution Algorithm
  - Generate array of File objects and sort array in reverse order
  - Build node priority array (min-heap)using pythons awesome heapq module
  	| * format for min-heap item is a triple of format (self.currentSpaceUsed,self.id, self)), where
    |   self - node object
    | * currentSpaceUsed = current space used, initialized to zero for all nodes until file is added
    | * id = unique id to be used by heap for prioritizing  in a situation where two items have the same 
    |   value for currentSpaceUsed

* Distribution algorithm description
  - For each file in already reverse sorted file array
     -Go through every node and if it fits into a node
     - update the given node's Node object
     - heapify min- heap(a.k.a refresh to maintain invariant)
     - break and move to next file in array
* Output format-
 - function output(inFileArray, outputFileName) prints the distribution plan to standard output or to file
  with name <outputFile> if it exists(or was indicated).

						===============
						Getting Started
						=============== 
 * All input files should be saves in /data_input directory, output files(if any) are saved in data-output
 *Run the following command in root directory (Davies_Odu/)

  > python solution.py -f <inputFile> -n <inputNode> -o <outputFile> 
  
  use option -h for help 
'''
import os, re, sys, getopt
from filehandler import *
import heapq

def main(argv):

	cl_arguments = parse(argv)

	#Extract file contents into file array(inFileArray) and node array(inNodeArray)
	(inFileArray, inNodeArray) = buildArrays(cl_arguments[0],cl_arguments[1])
	outputFileName  = cl_arguments[2]

	#get min-heap and reorganize file array in reverse sort
	nodeMinHeap = buildMinHeap(inNodeArray);
	inFileArray = sorted(inFileArray,reverse=True)
	
	if nodeMinHeap and inFileArray:
		distributeFiles(nodeMinHeap, inFileArray)
		output(inFileArray, outputFileName)

#python heapq module provides a neat min-heap
def buildMinHeap(inNodeArray):
	try:
		nodeMinHeap = []
		for node in inNodeArray:
			# add triples into array and prioritize
			heapq.heappush(nodeMinHeap, node.heapItem())
		return nodeMinHeap
	except:
		print("Error building min heap")


def distributeFiles(nodeMinHeap, inFileArray):
	#for each file in file array
	for file in inFileArray:
		try:
			#go over nodes in min-heap
			for i in range(len(nodeMinHeap)):
				currNode = nodeMinHeap[i][2]
				#if file fits into current node, store file , update min-heap and break for loop, moving to next file
				if file.size <= currNode.availSpace:
					currNode.storeFile(file)
					nodeMinHeap[i] = currNode.heapItem()
					heapq.heapify(nodeMinHeap)
					break
		except:
			print("Error in function with name : distributedFiles")
			sys.exit()


if __name__ == "__main__":
	main(sys.argv[1:])

__author__ = "Davies Odu"
__copyright__ = "copyright (C) March 2017 Davies Odu"
__email__ = "daviesodu@gmail.com"
