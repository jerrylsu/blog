#!/bin/sh

PID=$(ps -ef | grep jupyter-lab | grep -v grep | awk '{print $2}')
echo PID:$PID

kill -9 $PID
