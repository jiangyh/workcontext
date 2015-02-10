#!/bin/bash

#The comand to login to the guest
#nova ssh --private --login ubuntu -i ~/tmp/123.key controller
scp  yjiang5@otccloud06.sc.intel.com:/home/yjiang5/.ssh/* ~/.ssh/
sudo chown ubuntu /opt
sudo chgrp ubuntu /opt
sudo scp yjiang5@172.25.110.34:/etc/apt/sources.list /etc/apt/
sudo scp yjiang5@172.25.110.34:/etc/pip.conf /etc/
sudo apt-get install git
cd /opt
git clone ssh://yjiang5@172.25.110.34:/home/yjiang5/GITMIRROR/openstack-dev/devstack
cd devstack
mkdir files/images/
scp -r yjiang5@otccloud06.sc.intel.com:/home/yjiang5/work/openstack/devstack/files/images/* ./files/images/
scp -r yjiang5@otccloud06.sc.intel.com:/home/yjiang5/work/openstack/devstack/files/get-pip.py ./files/

