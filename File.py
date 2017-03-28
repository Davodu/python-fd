import os

# File object structure
class File(object):

	def __init__(self, name, size):
		self.name = name
		self.size = int(size)
		self.location = "unknown"



