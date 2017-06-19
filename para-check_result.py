import os
import argparse
import subprocess
import operator
import multiprocessing
def main(folder, name):
	result = os.path.join(folder,name)
	proc = subprocess.Popen(["/usa/yuewang/trec_eval.9.0/trec_eval","-m","map","/usa/yuewang/coretrack/qrel/robust04.qrel.txt",result], stdout=subprocess.PIPE)
	out, err = proc.communicate()
	(measure,dummy,value) = out.split()
	return value

if __name__ == '__main__':

	parser = argparse.ArgumentParser()
	parser.add_argument("-i",nargs='?',help='Result dir')
	args = parser.parse_args()
	folder = args.i

	pool = multiprocessing.Pool(processes=12)

	result={}
	for name in os.listdir(folder):
		result[name]=pool.apply_async(main,(folder, name))
	pool.close()
	pool.join()

	map_perf={}
	for item in result:
		map_perf[item]=result[item].get()
	sorted_map = sorted(map_perf.items(), key=operator.itemgetter(1),reverse=True)
	for key, value in sorted_map:
		print key + "\t" + value
