#!/bin/python

import os
import subprocess
import sys

start_count=1
def main():
	list_cmd = "grep \"submenu\\|^\\menuentry\" /boot/grub2/grub.cfg | cut -d \"'\" -f2"
	entries = subprocess.check_output(list_cmd, shell=True)
	lists = entries.splitlines()
	for count, entry in enumerate(lists, start=start_count):
		print '%s %s' % (count, entry)
	print '\nPlease select the default entry: [%s~%s]' % (start_count, len(lists))
	sel_item = sys.stdin.readline()
	try:
		item = int(sel_item)
	except ValueError:
		print "Wrong value, should be number between [%s~%s]" % (start_count, len(lists))
		return

	if item > len(lists) or item < start_count:
		print "%s is invalid, it should be %s~%s, exit now!" % (item, start_count, len(lists))
		return
	entry = lists[item - 1]
	cmd = "grub2-set-default \"%s\"" % entry
	return_value=subprocess.call(cmd, shell=True)

	if return_value:
		print "Failed to set with return value %s" % return_value
		return

	confirm = subprocess.check_output("grub2-editenv list", shell=True)
	sconfirm = confirm.split('=')
	if len(sconfirm)!= 2 or sconfirm[1].rstrip('\n') != entry:
		print "Error to setup the default "
		print "Wanted %s" % entry
		print "Got %s" % sconfirm
	else:
		print "We are done! The default entry is now"
		print sconfirm[1]

if __name__ == '__main__':
	main()
