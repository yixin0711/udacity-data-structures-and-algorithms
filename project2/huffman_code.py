import heapq
import copy
import sys

class HeapNode:

	def __init__(self, char, freq):
		self.char = char
		self.freq = freq
		self.left = None
		self.right = None

	def __lt__(self, other):
		return self.freq < other.freq

	def __gt__(self, other):
		return self.freq > other.freq

	def __eq__(self, other):
		if other is None:
			return False
		elif not isinstance(other, HeapNode):
			return False
		return self.freq == other.freq

class HuffmanTree:

	def __init__(self):

		self.heap = []
		self.codes = {}
		self.tree = None


	def set_dict(self, data):
		freq_dict = {}

		#check for every character in the string
		for char in data:
			#if the character is in the dict, frequency+1
			if char in freq_dict:
				freq_dict[char] += 1
			#if the char is new to the dict, set freq as 1
			else:
				freq_dict[char] = 1

		return freq_dict

	def make_heap(self, freq_dict):
		#make the dict to a heapq object
		for key in freq_dict:
			node = HeapNode(key, freq_dict[key])
			heapq.heappush(self.heap, node)

	def merge_nodes(self):

		while(len(self.heap)>1):
			#merge two min value 
			child0 = heapq.heappop(self.heap)
			child1 = heapq.heappop(self.heap)

			#make the parent node
			parent = HeapNode(child0.char+child1.char, child0.freq+child1.freq)
			parent.left = child0
			parent.right = child1

			#push the parent node back to the heap
			heapq.heappush(self.heap, parent)

		#make a copy of the heap tree for later use
		self.tree = copy.deepcopy(self.heap)

	#recursive method to get the encoding dict
	def encoding_helper(self, root, current_code):

		#base case 1
		if root is None:
			return
		#base case 2, when we reach a char, we want to set its code
		elif len(root.char) == 1:
			self.codes[root.char] = current_code

		#recursive step, when reaching a intermediate point, we traverse its left child and right child
		self.encoding_helper(root.left, current_code+"0")
		self.encoding_helper(root.right, current_code+"1")


	def huffman_encoding(self, data):

		if data == "":
			print("This is an empty text. No need for encoding.")
			return None, None
		elif not isinstance(data, str):
			print("Not valid data type. To encode, please insert a string.")
			return None, None

		#get the frequenct dict
		freq_dict = self.set_dict(data)
		#get the priority heap
		self.make_heap(freq_dict)
		#merge the nodes and get the huffman tree
		self.merge_nodes()

		#get a root to start
		root = heapq.heappop(self.heap)
		current_code = ""
		#call the helper function to do recursive
		self.encoding_helper(root, current_code)

		#combine the dict into a string for each char by sequence
		encoded_text = ""
		for char in data:
			encoded_text += self.codes[char]

		return encoded_text, self.tree


def huffman_decoding(code, tree=None):

	if code is None or tree is None:
		print("Invalid encoded data. Please check the original text.")
		return

	_tree = tree
	root = heapq.heappop(_tree)
	current_node = root

	decoded_text = ""

	for num in code:
		if num == "0":
			current_node = current_node.left
		elif num == "1":
			current_node = current_node.right
		if current_node.left is None:
			decoded_text += current_node.char
			current_node = root


if __name__ == "__main__":
    
    print ("==========Test 1==========")

    test1 = "AAAAAAABBBCCCCCCCDDEEEEEE"

    print ("The size of the data is: {}\n".format(sys.getsizeof(test1)))
    print ("The content of the data is: {}\n".format(test1))
    
    huffman_code = HuffmanTree()
    encoded_data, tree = huffman_code.huffman_encoding(test1)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    
    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
    print ("Test the functionality of this Huffman Encoding and Decoding...")
    print ("Passed!" if decoded_data == test1 else "Failed")
    
    
    print ("==========Test 2==========")

    test2 = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(test2)))
    print ("The content of the data is: {}\n".format(test2))
    
    huffman_code = HuffmanTree()
    encoded_data, tree = huffman_code.huffman_encoding(test2)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    
    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
    print ("Test the functionality of this Huffman Encoding and Decoding...")
    print ("Passed!" if decoded_data == test2 else "Failed")

    print ("==========Test 3, Corner Case for Empty Text==========")

    test3 = ""

    print ("The content of the data is: {}\n".format(test3))
    
    huffman_code = HuffmanTree()
    encoded_data, tree = huffman_code.huffman_encoding(test3)

    print ("The content of the encoded data is: {}\n".format(encoded_data))
    
    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The content of the encoded data is: {}\n".format(decoded_data))

    print ("==========Test 4, Corner Case for Invalid Data Type==========")

    test4 = HuffmanTree()

    print ("The content of the data is: {}\n".format(test3))
    huffman_code = HuffmanTree()
    encoded_data, tree = huffman_code.huffman_encoding(test4)
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The content of the encoded data is: {}\n".format(decoded_data))
    