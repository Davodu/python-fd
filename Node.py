import sys,re
import File
import itertools



'''
Node Object Structure
id  attribute to be used by heap for prioritizing in a situation where two items have the same value for currentSpaceUsed
'''
class Node(object):
	newid = itertools.count().next  #object level attibute

	def __init__(self, name, availSpace):

		#unique sequence count
		self.name = name
		self.availSpace = int(availSpace)
		self.currentSpaceUsed = 0
		self.id = Node.newid()

	def storeFile(self, file):
		self.currentSpaceUsed += file.size
		self.availSpace -= file.size
		file.location = self.name

	def heapItem(self):
		#triple representation of Node object for storage in priority array
		return (self.currentSpaceUsed,self.id, self)

		

