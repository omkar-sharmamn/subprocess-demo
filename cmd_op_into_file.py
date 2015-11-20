#!/usr/bin/python

import subprocess

def cmd_op_to_file(command, filename):
    """
    This module can be used to run a python file from another 
    .. python file and store the output into a file using 
    subprocess.
    """

    if command:
        args = command.split()
    else:
        return None

    try:
        with open(filename, "w") as fh:
            proc = subprocess.Popen(args, stdout=fh) 

    except IOError as e:
        print str(e)

    op = proc.communicate()[0]
    if proc.returncode == 0:
        return op
    else:
        return -1

if  __name__ == '__main__':
    filename = "/tmp/command_output"
    command = "python factorial.py"
    print cmd_op_to_file(command, filename)
    print "Ouput is written to : %s" % filename

