import sys
import Q1,Q2,Q3,Q4

def main(argv):
    global loglist
    loglist = []
    LoadFile()
    if(len(argv)<=1):
        print("argv Error!")
        return
    
    if(argv[1] == '1'):
        Q1.Question1(loglist)
    elif(argv[1] == '2'):
        N = 2 # set default Param here
        if(len(argv)>2):
            N = int(argv[2])
        Q2.Question2(loglist, N)
    elif(argv[1] == '3'):
        N = 2 
        m = 3 # set default Param here
        t = 200
        if(len(argv)>2):
            m = int(argv[2])
        if(len(argv)>3):
            t = int(argv[3])
        Q3.Question3(loglist, N, m, t)
    elif(argv[1] == '4'):
        N = 2 # set Param here
        if(len(argv)>2):
            N = int(argv[2])
        Q4.Question4(loglist, N)
    else:
        print("argv Error!")

    
def LoadFile():
    global loglist
    with open('test.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            log = line.rstrip().split(',')
            loglist.append(log)

if __name__ == '__main__':
    main(sys.argv)