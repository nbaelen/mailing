from datetime import datetime
startTime = datetime.now()

#do something
import time

print "Start : %s" % time.ctime()
time.sleep( 5 )
print "End : %s" % time.ctime()

#Python 2: 
print "End : %s" % (datetime.now() - startTime)

#Python 3: 
