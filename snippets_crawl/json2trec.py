# -*- coding: utf-8 -*-
import os
import json
import argparse
import codecs

def main(infolder,outfolder):
	
	for name in os.listdir(infolder):
		path_name = os.path.join(infolder, name)
		content = ""
		unique_content = {}
		google_result = path_name+"/google.json"
		with open(google_result) as google:	
			data = json.load(google)
			for i in xrange(0,len(data)):
				if not data[i]["snippets"] in unique_content:
					unique_content[data[i]["snippets"]] = 1
					content += "<DOC>\n"
					content += "<DOCNO>" + data[i]["id"] + "</DOCNO>\n"
					content += "<TEXT>" + data[i]["snippets"] + "</TEXT>\n"
					content += "</DOC>\n\n"

		yahoo_result = path_name+"/yahoo.json"
		with open(yahoo_result) as yahoo:	
			data = json.load(yahoo)
			for i in xrange(0,len(data)):
				if not data[i]["snippets"] in unique_content:
					unique_content[data[i]["snippets"]] = 1
					content += "<DOC>\n"
					content += "<DOCNO>" + data[i]["id"] + "</DOCNO>\n"
					content += "<TEXT>" + data[i]["snippets"] + "</TEXT>\n"
					content += "</DOC>\n\n"

		bing_result = path_name+"/bing.json"
		with open(bing_result) as bing:	
			data = json.load(bing)
			for i in xrange(0,len(data)):
				if not data[i]["snippets"] in unique_content:
					unique_content[data[i]["snippets"]] = 1
					content += "<DOC>\n"
					content += "<DOCNO>" + data[i]["id"] + "</DOCNO>\n"
					content += "<TEXT>" + data[i]["snippets"] + "</TEXT>\n"
					content += "</DOC>\n\n"

		output_file = os.path.join(outfolder, name)
		try:
			os.remove(output_file)
		except OSError:
			pass

		with codecs.open(output_file, 'w', 'utf-8') as out:
			out.write(content)  



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
