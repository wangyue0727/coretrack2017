import os
import argparse


def main(inputdir, outputdir):
	for name in os.listdir(inputdir):
		current_input = os.path.join(inputdir,name)
		current_output = os.path.join(outputdir,name)
		content = ""
		with open(current_input,"r") as infile:
			for line in infile:
				if "<index>" in line:
					line = "<index>/local/data/yuewang/coretrack/index/robust04/</index>"
				content += line + "\n"
		with open(current_output,"w") as outfile:
			outfile.write(content)

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", nargs='?', 
                        help="Input dir. ")
    parser.add_argument("-o", "--output", nargs='?', 
                        help="Output dir")
    args = parser.parse_args()
    inputdir = args.input
    outputdir = args.output
    main(inputdir, outputdir)
