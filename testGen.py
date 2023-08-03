import random
import copy

def main():
    # begin Param
    subnetNum = 3 # <10
    ipGroups = [ [10,20,30,0],[192,168,0,0],[123,45,78,0] ] # define the 1st ip of sub-net
    subnetPrefix = [16,20,24] # prefix length (how many swtichs)
    subnetServerNums = [3,4,6] # how many servers in same sub-net
    subnetDownPossibility = [1,2,3] # the % possibility of every switch    
    subnetDownLast = 3 # how long (call)

    serverDownPossibility = 5 # the % possibility of each server in sub-net
    serverDownLast = 3 # how long (call)
    serverOverloadPossibility = 15 # the % possibility of each server in sub-net
    serverOverloadLast = 5 # how long (call)

    beginTime = 20230101000000 # YYYYMMDDhhmmss
    subnetStep = 10 # 10s for each sub-net

    callNum = 10 # call of all sub-net, total=callNum*subnetNum
    timeStep = 200 # 1m for each call   
    # end Param

    subnetStatus = [] # record subnet down last time
    serverStatus = [] # record server down last time
    for i in range(subnetNum):
        serverStatus.append([])
        subnetStatus.append(0)
        for j in range(subnetServerNums[i]):
            serverStatus[i].append(0)

    with open('test.txt', 'w', encoding='UTF-8') as f:
        for i in range(callNum):
            callTime = beginTime + i * timeStep
            for j in range(subnetNum):
                subnetTime = callTime + j * subnetStep
                # if swtich down?
                subnetDown = True
                if(subnetStatus[j] > 0):
                    subnetStatus[j] -= 1                    
                else:
                    subnetDown = random.randint(0,100) <= subnetDownPossibility[j]
                    if(subnetDown):
                        subnetStatus[j] = subnetDownLast
                # loop for each server
                for k in range(subnetServerNums[j]):
                    curTime = str(subnetTime + k)
                    ip = getIP(ipGroups[j],k) + '/' + str(subnetPrefix[j])
                    if(subnetDown):
                        ping = '-'
                    else:
                        # if server down?
                        serverDown = False
                        if(serverStatus[j][k] > 0):
                            serverStatus[j][k] -= 1
                            serverDown = True
                        elif(random.randint(0,100) <= serverDownPossibility):
                            serverStatus[j][k] = serverDownLast # use +value
                            serverDown = True

                        if(serverDown):
                            ping = '-'
                        else:
                            # if server overload?
                            serverOverload = False
                            if(serverStatus[j][k] < 0):
                                serverStatus[j][k] += 1
                                serverOverload = True
                            elif(random.randint(0,100) <= serverOverloadPossibility):
                                serverStatus[j][k] = -serverOverloadLast # use +value
                                serverOverload = True

                            if(serverOverload):
                                ping = str(random.randint(300,999))
                            else:
                                ping = str(random.randint(1,200))

                    # output
                    f.write(','.join([curTime,ip,ping]))
                    f.write('\n')

def getIP(iplist, k):
    temp = copy.deepcopy(iplist)
    temp[3] = temp[3] + k
    return '.'.join(map(str,temp))


main()