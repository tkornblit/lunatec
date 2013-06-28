#!/usr/bin/python

import codecs, os


os.chdir("files/images")
for filename in os.listdir("."):
	new_name = filename.replace(" ","_").lower()
	os.rename(filename,new_name)

