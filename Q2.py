def Question2(loglist, N):
    timeoutDic = {}
    for log in loglist:
        date = log[0]
        ip = log[1]
        ping = log[2]
        if(ip not in timeoutDic):
            timeoutDic[ip] = ["", 0] # [date, time]

        if(ping == '-'): # timeout!
            if(timeoutDic[ip][0] == ""):
                # first timeout, record the date
                timeoutDic[ip] = [date, 0]
            else:
                timeoutDic[ip][1] += 1 # times +1
        else: # recovered!
            if(ip in timeoutDic and timeoutDic[ip][1] > N):# check if timeout > N
                startDate = timeoutDic[ip][0]
                print('Server {} Down! From:{}-{}'.format(ip,startDate,date))
                timeoutDic[ip] = ["", 0] # reset
