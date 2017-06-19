import multiprocessing
import time
import argparse
import os

def gen_exp(folder, M, R, K, beta):

    outputfile = folder+"exp-"+str(M)+"-"+str(R)+"-"+str(K)+"-"+str(beta)
    print "Working on ", outputfile 
    

    # External command
    # cmd = "./trec_query_expansion -oqf=../query/snippets-f2log.txt -orf=../results/snippets-f2log.txt -index_list=input_files/index_list.txt"
    # Check the range of beta


    # Internal command
    cmd = "./trec_query_expansion -oqf=../query/robust04-baseline-f2exp.txt -orf=../results/robust04-baseline-f2exp.txt -index_list=input_files/index_list_robust.txt"
    # Check the range of beta

    cmd += " -M=" +str(M)
    cmd += " -R=" +str(R)
    cmd += " -K=" +str(K)
    beta=beta/10.0
    cmd += " -beta=" + str(beta)
    cmd += " -output="+outputfile
    # print cmd
    os.system(cmd)

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('-i',nargs='?',help='query folder')
    args = parser.parse_args()
    folder = args.i

    pool = multiprocessing.Pool(processes=16)
    result = []
    for M in xrange(17,23):
        for R in xrange(15,25,2):
            for K in xrange(17,23):
                for beta in xrange(2,8): # [2,8] for internal expansion, and [12,18] for external expansion
                    filename = folder+"exp-"+str(M)+"-"+str(R)+"-"+str(K)+"-"+str(beta)
                    if not os.path.isfile(filename):
                        pool.apply_async(gen_exp, (folder, M, R, K, beta))
    pool.close()
    pool.join()
 
