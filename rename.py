#!/bin/env python

# Simple Python3.5+ code to parse a QBiC Samplesheet, use the OrganismID column to rename files with attached QBIC Barcodes for upload to qPortal/OpenBIS.
import os
import csv
import argparse
import glob

parser = argparse.ArgumentParser(description='Process QBiC samplesheet and rename files with it. Filenames should contain IDs of OrganismID in the FileName.')
parser.add_argument('samplesheet', help='The SampleSheet downloaded from qPortal with QBiC Barcodes attached.')
parser.add_argument('filepath', help='The Path to the folder with the files to rename.')
parser.add_argument('outputpath', help='The Path to the output folder with the files to copy to.')

args = parser.parse_args()

# Function to rename multiple files 
def main(): 
    with open(args.samplesheet, 'r') as f:
        reader = csv.DictReader(f, dialect='excel-tab')
        for row in reader:
            #print(row['QBiC Code'] +'\t' + row['Organism ID'])
            files = [g for g in glob.glob(args.filepath + "**/*" + row['Organism ID'] + "*")]
            for t in files:
                print(args.outputpath + row['QBiC Code'] + '_' + os.path.basename(t))
                os.rename(t,args.outputpath + row['QBiC Code'] + os.path.basename(t))

# Driver Code 
if __name__ == '__main__': 
	
	# Calling main() function 
	main() 
