#!/usr/bin/python3

import threading
import time
import requests

exitFlag = 0

class myThread (threading.Thread):
   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter
   def run(self):
      seeip_api(self.name, self.counter)

def seeip_api(threadName, counter):
   while counter:
      if exitFlag:
         threadName.exit()
      response = requests.get('http://34.80.123.23/api/myip')
      print ( "[%s] API/JSON response is %s" % ( threadName, response.json () ) )
      counter -= 1

def main():
    """Generate workload to http container
    in somewhere.
    """
    # Create new threads
    threads = []
    for i in range(10):
        threads.append( myThread(i, "Thread-1", 10) )

    # Start new Threads
    for t in threads:
        t.start()

    for t in threads:
        t.join()

    print ("Application processing...")

if __name__ == '__main__':
    main()
