#!/usr/bin/python
# Test to see if the network is up
# written for python 2.7.x 

import socket
import sys
import time
import argparse

# wait for the network to be fully up.
# works trying to get the ip address of a known site. default site is google.com.
# if unable to get the address, then sleep for a second and try again.
# will try until the timeout is reached.
# returns a tuple of two values: an integer return code and a string message.

MAX_TIMEOUT = 600
DEFAULT_TIMEOUT = 60
DEFAULT_WEB_SITE = 'www.google.com'

SUCCESS = 0
FAILURE = 1

def wait_for_network(timeout = DEFAULT_TIMEOUT, site = DEFAULT_WEB_SITE, debug = False):

  # create the socket to use for obtaining the ip address
  try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  except:
    return FAILURE, "socket create failed"

  # try to obtain the ip address of the site.
  while timeout > 0:
    if debug:
      print timeout
    timeout = timeout - 1
    try:
      remote_ip = socket.gethostbyname(site)
    except:      
      time.sleep(1)  # try again in another second
    else:      
      ip_msg = "ip address of " + site + " is " + remote_ip
      return SUCCESS, ip_msg
  return FAILURE, "unable to connect to the network"

# command line execution starts here
if __name__ == "__main__":

  parser = argparse.ArgumentParser(description = 'Wait for the network to come up')
  parser.add_argument('-t', '--timeout', type = int, default = DEFAULT_TIMEOUT, help = 'maximum time in seconds to wait before giving up')
  parser.add_argument('-w', '--website', default = DEFAULT_WEB_SITE, help = 'site to use for checking network status')
  parser.add_argument('-s', '--silent', action = 'store_true', help = 'if specified, do not display normal messages')
  parser.add_argument('-d', '--debug', action = 'store_true', help = 'if specified, display debugging messages')
  args = parser.parse_args()

  rc, msg = wait_for_network(args.timeout, args.website, args.debug)

  if not args.silent:
    print msg

  sys.exit(rc)
