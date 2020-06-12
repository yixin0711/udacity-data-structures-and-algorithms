import hashlib
import time

class Block:

	def __init__(self, timestamp=None, data=None, prev_hash=None):
		self.timestamp = timestamp
		self.data = data
		self.prev_hash = prev_hash
		self.hash = self.calc_hash()
		self.next = None

	def calc_hash(self):
		sha = hashlib.sha256()
		sha.update(self.data.encode('utf-8'))
		return sha.hexdigest()

	def __repr__(self):
		return (f'{self.__class__.__name__}('
				f'\nTime: {self.timestamp!r}, \nData: {self.data!r}, \nHash: {self.hash!r})')

class BlockChain:

	def __init__(self):
		self.head = None

	def get_head(self):
		return self.head

	def add_block(self, timestamp=None, data=None):

		if not isinstance(data, str):
			print("Invalid data type of inserted information. Please insert a string.")
			return

		if timestamp is None:
			print("Please insert the time when adding a block.")
			return

		if data is None or len(data) == 0:
			print("Please insert the information when adding a block.")
			return
			
		if self.get_head() is None:
			self.head = Block(timestamp, data, None)
		else:
			block = self.get_head()
			while block.next:
				block = block.next
			block.next = Block(timestamp, data, block.hash)

	def get_block(self, data=None):

		if not isinstance(data, str):
			print("Invalid data type of inserted information. Please insert a string.")
			return

		if data is None or len(data) == 0:
			print("Please insert the information you want to get.")
			return

		if self.get_head() is None:
			print("This is an empty Blockchain")
			return

		block = self.get_head()
		
		while block:
			if block.data == data:
				return block
			block = block.next

		print("No block found.")
		return


#test cases
#creat an empty block

myBlockChain = BlockChain()

print("==========Find a Block==========")
data1 = "Udacity"
time1 = time.time()
myBlockChain.get_block(data1)

print("==========Insert 1st block==========")
time1 = time.time()
myBlockChain.add_block(time1, data1)

print("==========Insert 2nd block==========")
data2 = "Data Structures and Algorithms Nanodegree"
time2 = time.time()
myBlockChain.add_block(time2, data2)

print("==========Insert 3rd block==========")
data3 = "Project 2"
time3 = time.time()
myBlockChain.add_block(time3, data3)

print("==========Find a block==========")
data4 = "Project 2"
print(myBlockChain.get_block(data4))

print("==========Find a block==========")
data5 = "Project 1"
print(myBlockChain.get_block(data5))

print("==========Corner case 1, Find an empty data block==========")
data6 = ""
print(myBlockChain.get_block(data6))

print("==========Corner case 2, invalid type of data==========")
data7 = BlockChain()
print(myBlockChain.get_block(data7))

print("==========Corner case 3, no time when adding==========")
data8 = "Block Chain"
print(myBlockChain.add_block(data = data8))