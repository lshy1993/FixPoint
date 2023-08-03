def Question3(loglist, N, m, t):
    timeoutDic = {}
    pingaveDic = {}
    for log in loglist:
        date = log[0]
        ip = log[1]
        ping = log[2]
        if(ip not in timeoutDic):
            timeoutDic[ip] = ["", 0]
        if(ip not in pingaveDic):
            pingaveDic[ip] = [[], ""] # [[ping..],date]

        if(ping == '-'): # timeout!
            if(timeoutDic[ip][0] == ""):
                # first time, record the date
                timeoutDic[ip] = [date, 0]
            else:                
                timeoutDic[ip][1] += 1 # times +1
        else: # noraml ping
            if(timeoutDic[ip][1] > N): # check if timeout times > N
                startDate = timeoutDic[ip][0]
                print('Server {} Down! From:{}-{}'.format(ip,startDate,date))
                timeoutDic[ip] = ["", 0] # reset

            if(timeoutDic[ip][1] > 0):
                # recover from down, reset pinglist
                pingaveDic[ip] = [[ping],""]
            else:
                pingaveDic[ip][0].append(ping)
            # cal the MovingAverage
            pinglist = pingaveDic[ip][0]
            count = len(pinglist)
            if(count == m):
                ave = sum(map(int,pinglist))/count
                pinglist.pop(0)
                startDate = pingaveDic[ip][1]
                if(ave > t):
                    # if first overload, then lable the date
                    if(startDate == ""):
                        pingaveDic[ip][1] = date
                else:
                    # if recover from overload, print date
                    if(startDate != ""):
                        print('Server {} Overload! From:{}-{}'.format(ip,startDate,date))