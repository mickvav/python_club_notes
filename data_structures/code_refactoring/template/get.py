#!/usr/bin/env python3
# 
# Use this script to download the data relevant to the project.
# 
# Now it contains a bunch of useful functions to download and extract data.
# Feel free to modify it to suit your needs.

import os
import sys
import urllib.request
import zipfile

def download_data():
	"""
	Download the data from the URL.
	"""
	# URL to download the data from
	url = "http://this.is.a.fake.url"
	# Directory to store the data
	directory = "data"
	# Path to the downloaded file
	file_path = os.path.join(directory, "data.zip")
	# Check if the directory exists
	if not os.path.exists(directory):
		os.makedirs(directory)
	# Download the data
	path, httpmessage = urllib.request.urlretrieve(url, file_path)
	# Extract the data
	if httpmessage.get_content_type() == 'application/zip':
		extract_data(file_path, directory)
	else:
		print("The downloaded file is not a zip file.")
		sys.exit(1)

def extract_data(path, directory):
	"""
	Extract the data from the zip file.
	"""
	with zipfile.ZipFile(path, 'r') as zip_ref:
		zip_ref.extractall(directory)
	# Remove the zip file
	os.remove(path)

if __name__ == "__main__":
	download_data()
