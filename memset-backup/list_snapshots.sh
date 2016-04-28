#!/bin/bash

/opt/ma-shell/ma-shell-master/build/scripts-2.7/ma-shell.py -k b08c5bd2eb6c460c90742f68a842de24 server.snapshot_list storage_name msipssoaa1|egrep -w snapshot_path > /var/log/backup/snapshot_log

