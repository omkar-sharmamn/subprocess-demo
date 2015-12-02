#!/usr/bin/python

import os
import subprocess
import sys

#  Return codes
#  1 : No command is given
# -1 : Error in command excecution or in command syntax 

def run_command(command=None):
    """
    This module runs the command input to it.
    On Success returns output 
    On failure returns -1
    On no input string passed returns 1
    """
  
    if command is None:
        print "command sent : ", command
        return 1 
    else:

        args = command.split()
        try:
            proc = subprocess.Popen(args, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
        except OSError as e:
            print
            print str(e), ": ", command

        try:
            proc
            op = proc.communicate()[0]
            ret_code = proc.returncode
            if ret_code == 0:
                return op
        except NameError:
            print "Command execution failed. " 
            return -1


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
        print
        print str(e)

    op = proc.communicate()[0]
    if proc.returncode == 0:
        return op
    else:
        return -1


def handle_ret_val(ret_val, command=None):
    """
    Function to handle return value.
    Prints message according to value inside ret_val.
    Returns nothing.
    """
 
    if ret_val == -1:
        print
        print "Command execution failed : %s" % command
    elif ret_val == 1:
        print
        print "No command is passed : %s" % command
    else:
        print
        print "Output of your input command \"%s\" : \n%s " % (command, ret_val)
 

def main():
 
    # For run_command       
    cmd1 = "lsa"
    ret_val = run_command(cmd1)
    handle_ret_val(ret_val, cmd1)  

    # For writing command output into a file
    filename = "/tmp/command_output"
    cmd2 = "/usr/bin/python factorial.py"

    ret_val_file =  cmd_op_to_file(cmd2, filename)
    handle_ret_val(ret_val_file, cmd2)  

    if os.path.exists(filename) :
        print
        print "Output is written to : %s" % filename
      

if  __name__ == '__main__':
    main()


















