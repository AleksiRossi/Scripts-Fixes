#!/usr/bin/python

# Take a snapshot of a server and write log into /var/log/backup/

from xmlrpclib import ServerProxy
from time import sleep
from datetime import datetime
import sys
import time

KEY = "b08c5bd2eb6c460c90742f68a842de24"
URI = "https://%s:@api.memset.com/v1/xmlrpc" % KEY
SNAME = sys.argv[1]
TYPE = sys.argv[2]
LOG = sys.argv[3]

def main():
    s = ServerProxy(URI)
    r = s.server.snapshot(dict(name=SNAME, storage_name='msipssoaa1', image_type=TYPE))

    while not r['finished']:
        sleep(600)
        r = s.job.status(dict(id=r['id']))
        string = str(r)
	time = datetime.now().strftime('%Y-%m-%d_%H:%M:%S - ')
        with open('/var/log/backup/'+LOG, 'a') as logfile:
		logfile.write(time + string + '\n')
    with open ('/var/log/backup/'+LOG, 'a') as logfile:
	logfile.write('snapshot DONE!\n')
 
if __name__ == "__main__":
    main()
