import os
import argparse

def main(folder):

    for name in os.listdir(folder):
        queryfile = os.path.join(folder,name)
        cmd = "/usa/yuewang/coretrack/indri/bin/bin/IndriRunQuery "
        cmd += queryfile
        if not os.path.exists("/local/data/yuewang/coretrack/results/"+folder):
            os.makedirs("/local/data/yuewang/coretrack/results/"+folder)
        cmd += " > /local/data/yuewang/coretrack/results/" + queryfile
        #print cmd
        print "Working on " + queryfile
        os.system(cmd)

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i',nargs='?',help='query folder')
    args = parser.parse_args()
    folder = args.i
    main(folder)
