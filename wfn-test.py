#!/usr/bin/python
# Test to see if the network is up
# written for python 2.7.x 

import wfn

print "Test of default parameters"
rc, msg = wfn.wait_for_network()

print "return code from wfn is ", rc
print "return message: " + msg

print "Test with different site specified"
rc, msg = wfn.wait_for_network(site = 'www.facebook.com')

print "return code from wfn is ", rc
print "return message: " + msg

print "Test with non-reachable site specified, 5 second timeout, and debug messages on"
rc, msg = wfn.wait_for_network(timeout = 5, site = 'www.fdjhfsdj.com', debug = True)

print "return code from wfn is ", rc
print "return message: " + msg

print "Test with non-reachable site specified, 5 second timeout"
rc, msg = wfn.wait_for_network(5, 'www.fdjhfsdj.com')

print "return code from wfn is ", rc
print "return message: " + msg