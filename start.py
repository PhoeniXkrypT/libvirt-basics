import libvirt
import sys

conn = libvirt.open("xen:///")
if conn == None:
    print 'Failed to open connection to the hypervisor'
    sys.exit(1)

xmlfile = sys.argv[1]
fp = open(xmlfile, "r")
xml = fp.read()
fp.close()

dom = conn.createLinux(xml, 0)
