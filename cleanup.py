#!/usr/bin/env python
import os
import re

def reportJsFiles():	

	jsfiles = []
	usedfiles = []

	htmlfiles = []
	htmlregex = r'.\.html'

	# go through and get all the html file paths
	for root, dirs, files in os.walk('.'):
		for file in files:
			if re.search(htmlregex, file):
				htmlfiles.append(os.path.join(root, file))

	# get all the script files
	for root, dirs, files in os.walk('scripts'):
		for file in files:
			# print(file)
			jsfiles.append(file)

	# go over the html files
	# read file, go over js files and see if file matches
	# if yes, check for jsfile in used files list and add if needed
	print("-----USED")
	for htmlfile in htmlfiles:
		fopen = open(htmlfile, 'r')
		lines = fopen.read()
		for jsfile in jsfiles:
			if lines.find(jsfile) > 0:
				# print(jsfile + " in " + htmlfile)
				if jsfile not in usedfiles:
					usedfiles.append(jsfile)
					print(jsfile)

	# print all the js files that are not in used files
	print("-----UNUSED")
	for jsfile in jsfiles:
		if jsfile not in usedfiles:
			print(jsfile)


	

if __name__ == '__main__':
		reportJsFiles()