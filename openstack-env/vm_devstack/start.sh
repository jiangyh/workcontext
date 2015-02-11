#!/bin/bash

#The comand to login to the guest
#nova ssh --private --login ubuntu -i ~/tmp/123.key controller
`sudo cp pip.conf /etc/`
`scp  yjiang5@otccloud06.sc.intel.com:/home/yjiang5/.ssh/* ~/.ssh/`
`sudo chown ubuntu /opt`
`sudo chgrp ubuntu /opt`
`sudo scp yjiang5@otccloud06.sc.intel.com:/etc/apt/sources.list /etc/apt/`
`sudo scp yjiang5@otccloud06.sc.intel.com:/etc/pip.conf /etc/`
`sudo apt-get update`
#`sudo sh -c 'echo "auth_tcp = \"none\"" >>/etc/libvirt/libvirtd.conf'`
#`sudo sh -c 'echo "listen_tcp = 1" >>/etc/libvirt/libvirtd.conf'`
#`sudo sh -c 'echo "listen_tls = 0" >>/etc/libvirt/libvirtd.conf'`
`sudo apt-get install git`
`cd /opt; git clone ssh://yjiang5@otccloud06.sc.intel.com:/home/yjiang5/GITMIRROR/openstack-dev/devstack`
`cd /opt/devstack; mkdir files/images/`
`scp -r yjiang5@otccloud06.sc.intel.com:/home/yjiang5/work/openstack/devstack/files/images/* /opt/devstack/files/images/`
`scp -r yjiang5@otccloud06.sc.intel.com:/home/yjiang5/work/openstack/devstack/files/get-pip.py /opt/devstack/files/`

