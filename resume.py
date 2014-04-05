import libvirt
import sys

conn = libvirt.open("xen:///")
if conn == None:
    print 'Failed to open connection to the hypervisor'
    sys.exit(1)

dom_name = sys.argv[1]

print "Domain name " + dom_name + " starts resuming..."
domain = conn.restore(dom_name)
print "Domain name " + dom_name + " resumed..."
