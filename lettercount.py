
from sys import argv
import string
script, filename = argv

txt = open(filename)
filetext = txt.read()


for letter in "abcdefghijklmnopqrstuvwxyz":
	 count = 0
	 for char in filetext:
	 	if string.lower(char) == letter:
	 		count += 1
	 print count

