import os
from subprocess import call

root="MRK-internal-f2log/"
if not os.path.exists(root):
    os.makedirs(root)
# M=20
# R=19
# K=20
beta=5
beta = beta/10.0

for M in xrange(18, 23):
	for R in xrange(15,25,2):
		for K in xrange(18,23):
# for beta in xrange(1,20):
			outputfile = root+"exp-"+str(M)+"-"+str(R)+"-"+str(K)+"-"+str(beta)
			
			# External command
			# cmd = "./trec_query_expansion -oqf=../query/snippets-f2log.txt -orf=../results/snippets-f2log.txt -index_list=input_files/index_list.txt"
			# Internal command
			cmd = "./trec_query_expansion -oqf=../query/robust04-baseline-f2log.txt -orf=../results/robust04-baseline-f2log.txt -index_list=input_files/index_list_robust.txt"
			cmd += " -M=" +str(M)
			cmd += " -R=" +str(R)
			cmd += " -K=" +str(K)
			cmd += " -beta=" + str(beta)
			cmd += " -output="+outputfile
			#print cmd
			os.system(cmd)



