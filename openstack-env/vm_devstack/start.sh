#!/bin/bash

source ./start.rc

TOP_DIR=$(cd $(dirname "$0") && pwd)

#The comand to login to the guest
#nova ssh --private --login ubuntu -i ~/tmp/123.key controller
sudo cp pip.conf /etc/
# No idea why the virtualenv will use so old pip which only support pip.conf at per-user base
mkdir ~/.pip/
cp pip.conf ~/.pip/
cp pydistutils.cfg ~/.pydistutils.cfg

scp  yjiang5@otccloud06.sc.intel.com:/home/yjiang5/.ssh/* ~/.ssh/
sudo chown ubuntu /opt
sudo chgrp ubuntu /opt
sudo scp yjiang5@otccloud06.sc.intel.com:/etc/apt/sources.list /etc/apt/
sudo apt-get update
#`sudo sh -c 'echo "auth_tcp = \"none\"" >>/etc/libvirt/libvirtd.conf'`
#`sudo sh -c 'echo "listen_tcp = 1" >>/etc/libvirt/libvirtd.conf'`
#`sudo sh -c 'echo "listen_tls = 0" >>/etc/libvirt/libvirtd.conf'`
sudo apt-get install git


cd /opt;
git clone $DEVSTACK_REPO
cd /opt/devstack
git checkout $DEVSTACK_BRANCH

mkdir files/images/
scp -r yjiang5@otccloud06.sc.intel.com:/home/yjiang5/work/openstack/devstack/files/images/* /opt/devstack/files/images/
scp -r yjiang5@otccloud06.sc.intel.com:/home/yjiang5/work/openstack/devstack/files/c*.gz /opt/devstack/files/
scp -r yjiang5@otccloud06.sc.intel.com:/home/yjiang5/work/openstack/devstack/files/F*.qcow2 /opt/devstack/files/
scp -r yjiang5@otccloud06.sc.intel.com:/home/yjiang5/work/openstack/devstack/files/get-pip.py /opt/devstack/files/
