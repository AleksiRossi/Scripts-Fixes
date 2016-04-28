#!/usr/bin/python

import os, sys, time, re
from time import strptime, sleep
from datetime import datetime, timedelta
from xmlrpclib import ServerProxy

KEY = "b08c5bd2eb6c460c90742f68a842de24"
URI = "https://%s:@api.memset.com/v1/xmlrpc" % KEY
cutoff = datetime.now() - timedelta(days=14)
file = "/var/log/backup/snapshot_log"
s = ServerProxy(URI)

with open(file) as f:
	for line in f:
		match = re.search(r'\d{4}-\d{2}-\d{2}-\d{2}-\d{2}-\d{2}', line)
		date = datetime.strptime(match.group(), '%Y-%m-%d-%H-%M-%S')
		path = line[22:-4] 
		if cutoff > date:
			delete = s.server.snapshot_delete(dict(storage_name='msipssoaa1', snapshot_path=path))
			while not delete['finished']:
				sleep(120)
				delete = s.job.status(dict(id=delete['id']))
				string = str(delete)
				time = datetime.now().strftime('%Y-%m-%d_%H:%M:%S - ')
				with open('/var/log/backup/delete_log', 'a') as log:
					log.write(time + path + " - " + string +'\n')
			with open('/var/log/backup/delete_log', 'a') as log:
				log.write('snapshot deleted!\n')
			break
	else:
		with open('/var/log/backup/delete_log', 'a') as log:
			log.write(' - Snapshot action already on or no more snapshots\n\\')
