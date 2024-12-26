#!/usr/bin/env python3
#
# Use this script to process the data relevant to the project.
# 

import os
import sys
import glob

class Loader:
	"""
	Load the data from the directory.
	"""
	def __init__(self, directory):
		"""
		Initialize the Loader class.
		"""
		self.directory = directory

	def load_data(self):
		"""
		Load the data from the directory.

		Usage:
		loader = Loader(directory)
		data = loader.load_data()
		print(data)
		"""
		# Check if the directory exists
		if not os.path.exists(self.directory):
			print("The directory does not exist.")
			sys.exit(1)
		# Read the data
		data = []
		for file in os.listdir(self.directory):
			with open(os.path.join(self.directory, file), 'r') as f:
				data.append(f.read())
		return data
	
	def file_reading_iterator(self):
		"""
		Return a file reading iterator.

		Usage:
		loader = Loader(directory)
		for filename, data in loader.file_reading_iterator():
			print(filename, data)
		"""
		for file in os.listdir(self.directory):
			with open(os.path.join(self.directory, file), 'r') as f:
				yield file, f.read()

	def masked_reading_iterator(self, mask):
		"""
		Return a file reading generator.

		Usage:
		loader = Loader(directory)
		for filename, data in loader.masked_reading_iterator("*.txt"):
			print(filename, data)
		"""
		for file in glob.iglob(os.path.join(self.directory, mask)):
			with open(os.path.join(self.directory, file), 'r') as f:
				yield file, f.read()

class ProcessedData:
	"""
	Process the data.
	"""
	def __init__(self, filename, data):
		"""
		Initialize the ProcessedData class.
		"""
		self.filename = filename
		self.data = data

	def process_data(self):
		"""
		Process the data.

		Usage:
		processed_data = ProcessedData(filename, data)
		processed_data.process_data()
		"""
		print(f"Processing {self.filename}")
		print(self.data)
		self.result = len(self.data) # ! only example

class ReduceData:
	"""
	Use this class to gather some statistics about the data.
	"""
	def __init__(self, name):
		self.name = name
		self.reduced_data = {} # ! only example

	def process_chunk(self, chunk, chunk_name):
		"""
		Process a chunk of data.

		Usage:
		reducer = ReduceData(name)
		reducer.process_chunk(chunk, chunk_name)
		"""
		# Process the chunk
		self.reduced_data[chunk_name] = len(chunk) # ! only example
		pass

	def get_statistics(self):
		"""
		Return the statistics.

		Usage:
		reducer = ReduceData(name)
		reducer.get_statistics()
		"""
		return self.reduced_data
	
	
class Saver:
	"""
	Save the processed data.
	"""
	def __init__(self, directory):
		"""
		Initialize the Saver class.
		"""
		self.directory = directory

	def save_data(self, processed_data):
		"""
		Save the processed data.

		Usage:
		saver = Saver(directory)
		saver.save_data(processed_data)
		"""
		if not os.path.exists(self.directory):
			os.makedirs(self.directory)
		with open(os.path.join(self.directory, processed_data.filename), 'w') as f:
			f.write(str(processed_data.result))