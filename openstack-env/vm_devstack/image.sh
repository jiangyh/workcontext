#!/bin/bash
rid=`glance image-create --name cirros.root --disk-format ari --container-format ari --file ./cirros-0.3.2-x86_64-initrd`
echo "ramdisk is $rid"
kid=`glance image-create --name cirros.kernel --disk-format aki --container-format aki --file ./cirros-0.3.2-x86_64-vmlinuz`
echo "kernel is $kid"
#image=`glance image-create --name cirros --disk-format ami --container-format ami --file ./cirros-0.3.2-x86_64-blank.img --property kernel_id\=$kid --property  ramdisk_id\=$rid`
#echo "Image is $image"
