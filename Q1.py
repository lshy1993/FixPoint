def Question1(loglist):
    timeoutDic = {}
    for log in loglist:
        date = log[0]
        ip = log[1]
        ping = log[2]
        if(ip not in timeoutDic):
            timeoutDic[ip] = ""
        if(ping == '-'): # timeout!
            if(timeoutDic[ip] == ""):
                # first timeout, record the date
                timeoutDic[ip] = date
        else:
            # check if recover from timeout
            if(timeoutDic[ip] != ""):
                startDate = timeoutDic[ip]
                print('Server {} Down! From:{}-{}'.format(ip,startDate,date))
                timeoutDic[ip] = ""