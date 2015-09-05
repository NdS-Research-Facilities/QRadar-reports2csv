# python3 script
# Nico de Smidt 2015

import sys, os
import json, time
from xml.etree.ElementTree import ElementTree
import xml.etree.ElementTree as ET
import lxml.etree as etree
import tarfile

from array import array
from types import *
from optparse import OptionParser

import pprint

def main():

	tar = tarfile.open(sys.argv[1], "r:gz")
	for tarinfo in tar:
		if "/" not in tarinfo.name and tarinfo.isreg():
			mainfile=tarinfo.name
	with tar.extractfile(mainfile) as myfile:
#		print(myfile)
		tree = ET.parse(myfile)
#		print(tree)
		root = tree.getroot()
#		print(ET.dump(root))
		for reportfile in root.findall('./report/filedata'):
#			print(reportfile.text)
			with tar.extractfile(reportfile.text) as mycontentfile:
				contenttree = ET.parse(mycontentfile)
				contentroot = contenttree.getroot()
#				print(ET.dump(contentroot))
				contentName= contentroot.find("*/void[@property='title']/string")
#				print('"'+str(contentName.text)+'"')
				contentDescription= contentroot.find("*/void[@property='descrition']/string")
				print('"'+str(contentName.text)+'","'+str(contentDescription.text)+'"')


if __name__ == "__main__":
    main()
