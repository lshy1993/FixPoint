def Question4(loglist,N):
    subnetDic = {}
    for log in loglist:
        date = log[0]
        ip = log[1]
        ping = log[2]
        network = getNetwork(ip)
        if(network not in subnetDic):
            # init subnet
            subnetDic[network] = {}
        subnetStatus = subnetDic[network]
        if(ip not in subnetStatus):
            subnetStatus[ip] = ["", 0, True] # struct:[date, times, recoverd]
        if(ping == '-'): # timeout!
            if(subnetStatus[ip][0] == ""):
                # record [first date, times=1, recoverd=F]
                subnetStatus[ip] = [date, 1, False]
            else:
                # times +1
                subnetStatus[ip][1] += 1
        else: # recovered!
            # check if ALL server timeout > N
            if(checkAllServer(subnetStatus, N)):
                startDate = getSubnetDownDate(subnetStatus)
                print('Sub-Net {} Down! From:{}-{}'.format(network,startDate,date))
                subnetStatus[ip] = ["", 0, True] # reset
            subnetStatus[ip][2] = True
                    
def getNetwork(ipstr):
    temp = ipstr.split('/')
    iplist = temp[0].split('.')
    ipint = (int(iplist[0]) << 24) + (int(iplist[1]) << 16) + (int(iplist[2]) << 8) + int(iplist[3])

    prefix = int(temp[1])
    subnet = (2 ** prefix - 1) << (32 - prefix)
    
    networkAddress = ipint & subnet
    networkList = [(networkAddress >> 24) & 255, (networkAddress >> 16) & 255, (networkAddress >> 8) & 255, networkAddress & 255]
    networkStr = '.'.join(map(str, networkList))

    return networkStr

def checkAllServer(subnetStatus, N):
    if len(subnetStatus) == 0:
        return False
    for server in subnetStatus.values():
        if(server[2]):
            return False # any server Already check return False
        if(server[1] <= N):
            return False
    return True

def getSubnetDownDate(subnetStatus):
    maxdate = 0
    for server in subnetStatus.values():
        maxdate = max(maxdate, int(server[0]))
    return maxdate