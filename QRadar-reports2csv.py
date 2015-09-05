#
# QRadar python3 script to retrieve all report templates available in QRadar
# Nico de Smidt 20150905
#
# run this script on a python3 enabled machine, this is typically not a QRadar appliance
# Usage: pyhton3 QRadar-reports2csv.py [report-ContentExport-date.tar.gz] > reports.csv
# where [report-ContentExport-date.tar.gz] is derived by running:
# ./contentManagement.pl --action export --content-type report --id all
# on your QRadar system, and copy the resulting .tar.gz file to your python3 machine
#

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
		tree = ET.parse(myfile)
		root = tree.getroot()
		for reportfile in root.findall('./report/filedata'):
			with tar.extractfile(reportfile.text) as mycontentfile:
				contenttree = ET.parse(mycontentfile)
				contentroot = contenttree.getroot()
				contentName= contentroot.find("*/void[@property='title']/string")
				contentDescription= contentroot.find("*/void[@property='descrition']/string")
				print('"'+str(contentName.text)+'","'+str(contentDescription.text)+'"')

if __name__ == "__main__":
    main()
