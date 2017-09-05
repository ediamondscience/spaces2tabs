#spaces2tabs.py
#A tool for correcting the indentation of multiple python files at once. 
#Use: python spaces2tabs.py file0.py file1.py file2.py etc...


import sys


#get all command line args
args=sys.argv

#pop the name of this file
args.pop(0)

#go through and open each file
for filename in args:

	with open(filename, 'r') as f:

		#use a ist as a line buffer and collect all lines in a file 
		linebuff=[]
		for line in f:
			#adjust each line to replace four spaces with a tab before placing it in the buffer
			linebuff.append(line.replace('    ','	'))
		
		#create a new file name using the old one
		newfilename=filename.strip('.py')+'_tabs.py'

		#sequentially write line buffer to file
		with open(newfilename, 'w') as nf:
			for l in linebuff:
				nf.write(l)
