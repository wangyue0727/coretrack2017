import multiprocessing
import time
import argparse
import os

def runquery(cmd):

    print cmd
    os.system(cmd)
    return            


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('-i',nargs='?',help='query folder')
    args = parser.parse_args()
    folder = args.i

    pool = multiprocessing.Pool(processes=8)

    for name in os.listdir(folder):
        queryfile = os.path.join(folder,name)
        cmd = "~/coretrack/indri/bin/bin/IndriRunQuery "
        cmd += queryfile
        if not os.path.exists("/infolab/headnode/yuewang/coretrack/results/"+folder):
            os.makedirs("/infolab/headnode/yuewang/coretrack/results/"+folder)
        cmd += " > /infolab/headnode/yuewang/coretrack/results/" + queryfile
        pool.apply_async(runquery,(cmd, ))

    pool.close()
    pool.join()
 
