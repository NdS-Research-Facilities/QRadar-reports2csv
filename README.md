# QRadar-reports2csv
Convert a CMT export file to a .csv file to be imported into a spreadsheet

This script requires a contentManagement export file in order to process into a .csv file which lists all standard report templates.

Run below command on a QRadar appliance

/opt/qradar/bin/contentManagement.pl --action export --content-type report --id all

copy the resulting .tar.gz file to a python3 enabled machine (this is typically not your QRadar machine)
on this machine run this script as:

pyhton3 QRadar-reports2csv.py [report-ContentExport-date.tar.gz] > reports.csv

where [report-ContentExport-date.tar.gz] = the file you copied from your QRadar machine

open reports.csv in a spreadsheet and format at will.

Any feedback is welcome
