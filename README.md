# waitfornetwork

## Overview
*waitfornetwork* is a program used to determine if the ip network is up. *waitfornetwork* will attempt to get the IP address of a site, retrying for a specified number of seconds, until either the IP address is obtained or the time has been exceeded. 

This program was intended to be used in boot scripts like *rc.local* before programs are invoked that need access to the network. Using *waitfornetwork* is better than using adding *post-up* commands to */etc/network/interfaces* because *waitfornetwork* is not tied to a specific network interface and is not as difficult to use or test.

*waitfornetwork* is written for python 2.7.x.

## Usage Instructions

*waitfornetwork* can be executed from the command line or as a function imported by another python program.

### Command Line Usage:

    $ python wfn.py -h

    usage: wfn.py [-h] [-t TIMEOUT] [-w WEBSITE] [-s] [-d]

    Wait for the network to come up

     optional arguments:
      -h, --help            show this help message and exit
      -t TIMEOUT, --timeout TIMEOUT
                            maximum time in seconds to wait before giving up
      -w WEBSITE, --website WEBSITE
                            site to use for checking network status
      -s, --silent          if specified, do not display normal messages
      -d, --debug           if specified, display debugging messages   
    
#### Command Line Examples
Wait for the network to become available using the default parameters: 60 second timeout, check www.google.com, display normal message, don't display debugging messages.

    $ python wfn.py

Wait for the network to become available using a 600 second timeout, the default site, silent mode, and no debug messages displayed.

    $ python wfn.py -t 600 -s

Wait for the network to become available using the default timeout, a specified site, display normal messages, and no debugging messages displayed.

    $ python wfn.py -w www.facebook.com

Wait for the network to become available using the default timeout, the default site, display normal messages, but display debugging messages.

    $ python wfn.py -d

#### Messages
If *wfn.py* completes successfully, *wfn.py* will display a message like:

    ip address of www.google.com is 216.58.193.68

and return 0 for the error code.

If *wfn.py* times out trying to obtain the IP address of the site, *wfn.py* will display an error message like: 

    unable to connect to the network

and return 1 for the error code.

If *wfn.py* is unable to create a socket, *wfn.py* will display an error message like:

    socket created failed

and return 1 for the error code.

### Python usage:
#### Syntax
    wait_for_network(timeout = DEFAULT_TIMEOUT, site = DEFAULT_WEB_SITE, debug = False)

    timeout   number of seconds before giving up 
              default is 240 seconds
    site      string with the name of the web site to try to get it's IP address
              default is www.google.com
    debug     boolean indicating whether to display debug messages
              default is not to display debugging messages
#### Examples
Wait for the network to become available using the default parameters: 240 second timeout, check www.google.com, don't display debugging messages.

    import wfn
    rc, msg = wfn.wait_for_network()

Wait for the network to become available using a 400 second timeout, the default site, and no debug messages displayed.

    import wfn
    rc, msg = wfn.wait_for_network(timeout=400)
    
Wait for the network to become available using the default timeout, a specified site, display normal messages, and no debugging messages displayed.

    import wfn
    rc, msg = wfn.wait_for_network(site='www.facebook.com')
    
Wait for the network to become available using the default timeout, the default site, display normal messages, but display debugging messages. 
  
    import wfn
    rc, msg = wfn.wait_for_network(debug=True)

Wait for the network to become available using a specified site, a timeout of 600 seconds, and debugging messages displayed.

    import wfn
    rc, msg = wfn.wait_for_network(timeout=600, site=www.facebook.com, debug=True)

## Installation Instructions

Change to the directory where you want the files to be installed.

Install *wfn.py* and the associated files by cloning this repository with this command:

    $ git clone https://github.com/makeralchemy/waitfornetwork

Verify everything has installed properly by issuing the command:

    $ python wfn.py


## License
This project is licensed under the MIT license.

