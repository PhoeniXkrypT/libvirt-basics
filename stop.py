import libvirt
import sys

conn = libvirt.open("xen:///")
if conn == None:
    print 'Failed to open connection to the hypervisor'
    sys.exit(1)

dom_name = sys.argv[1]
dom = conn.lookupByName(dom_name)
dom.shutdown()

print "Domain name " + dom_name + " is shutting down..."
