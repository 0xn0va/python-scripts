import sys
import socket
import getopt
import threading
import subprocess

listen = False
command = False
upload = False
execute = ""
target = ""
upload_destination = ""
port = 0

def usage():
    print "python netcat from BHP book"
    print
    print "Usage: pync.py -t target_host -p port"
    print "-l --listen              - listen on [host]:[post] " \
                                      "for incoming connections"
    print 