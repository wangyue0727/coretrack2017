# -*- coding: utf-8 -*-
import os
import json
import argparse
import codecs
import shutil

def main(infolder,outfolder):
	
	for name in os.listdir(infolder):
		path_name = os.path.join(infolder, name)
		content = ""
		google_result = path_name+"/google.json"

		output_file = os.path.join(outfolder, name)

		# print "copy " + google_result + " to " + output_file

		shutil.copy(google_result, output_file)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--output_folder", nargs=1, 
                        help="Output folder for the TREC-format Snippets")
    parser.add_argument("-i", "--input_folder", nargs=1, 
                        help="Input folder that contains the snippets in JSON format")
    args = parser.parse_args()
    outfolder = args.output_folder[0]
    infolder = args.input_folder[0]

    main(infolder,outfolder)
