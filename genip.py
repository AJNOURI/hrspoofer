#!/usr/bin/python

__author__ = "AJN (ajn.bin@gmail.com): cciethebeginning.wordpress.com"

from ipaddr import *
import csv
import random
import sys
 
total_args = len(sys.argv)
print total_args

if total_args != 4:
    print "\n"
    print "Usage: ./%s <X.X.X.X/mask> <output_int> <output_file.csv>" %sys.argv[0]
    print "    X.X.X.X/mask      : the subnet from which you want to generate the ip addresses."
    print "    output_int        : the egress interface receiving the generated secondary addresses."
    print "    output_file.csv   : The resulting file containing ip,port.\n"
    sys.exit(1)


print "#!/usr/bin/python"
subn=IPNetwork(sys.argv[1])
netmask=subn.prefixlen
with open(sys.argv[3], 'w') as ip_port_file:
    csv_data = csv.writer(ip_port_file, delimiter=',')
    for ip in subn:
        srcport=random.randrange(32768,61000)
        srcip=ip
        sock=[srcip,srcport]
	csv_data.writerow(sock)
	print 'ip addr add %s/%s dev %s' %(ip,netmask,sys.argv[2])

