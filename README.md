# QRadar-reports2csv
Convert a CMT export file to a .csv file to be imported into a spreadsheet

This script requires a contetentManagemnt script export file inorder to process this file into a .csv file which lists all standard report templates.

Run below command on a QRadar appliance
./contentManagement.pl --action export --content-type report --id all

copy the resulting file to a python3 enabled machine (this is typically not your QRadar machine)
on this machine run this script as:
pyhton3 QRadar-reports2csv.py [report-ContentExport-date.tar.gz] > reports.csv
where [report-ContentExport-date.tar.gz] = the file you copied from your QRadar machine

open reports.csv in a spreadsheet and format at will.

