#!/bin/bash
sudo taskset -c 2 /usr/local/bin/stress -c 1 -m 1  -d 1 &
sudo taskset -c 2 /usr/local/bin/cyclictest -t1 -p 80 -n -i 2000 -l 100000 
