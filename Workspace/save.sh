#!/bin/bash

BACKUPTIME=`date +%b-%d-%y` 
DESTINATION=/home/pwned/backup-$BACKUPTIME.tar.gz 

SOURCEFOLDER=/home/pwned/Desktop

tar -cpzf $DESTINATION $SOURCEFOLDER 

