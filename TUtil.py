from datetime import datetime

#Return (int) seconds since 1st january 1970 (Known as Posix Time, Unix epoch, Unix Timestamp)
def getUnixTimeStamp():
    now = datetime.now()
    return int(datetime.timestamp(now))

#Return (float) seconds since 1st january 1970 (Known as Posix Time, Unix epoch, Unix Timestamp)
def getUnixTimeStampFloat():
    now = datetime.now()
    return datetime.timestamp(now)

def getTimeStamp(format=None):
    if(format==None):
        return datetime.now().strftime("%Y%m%d%H%M%S.%f")
    else:
        return datetime.now().strftime(format)

#Return 2020-01-12 19:11:39.239338
def getDateTime(): 
    return datetime.now()

#Return 2020-01-12
def getDate(): 
    return datetime.now().date()

#Return 19:11:39
def getTime(): 
    return datetime.now().strftime("%X")

#Return 19:11:39.239338
def getTimeMs(): 
    return datetime.now().time()