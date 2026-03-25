#!/usr/bin/python3

# INET4031
# Adonay Bereket
# Date Created
# Date Last Modified

# os lets the script run Linux commands
# re is used for checking patterns like lines that start with #
# sys lets the script read the input file line by line

import os
import re
import sys

def main():

    # Ask the user if they want to do a dry run.
    # Y means just print the commands so we can see what would happen.
    # N means actually run the commands and create the users.
    dry_run = input("Run dry-run? (Y/N): ").strip().upper()

    for line in sys.stdin:

        # Check if the line starts with # which means it is a comment
        match = re.match("^#", line)

        # Clean up the line and split it into fields using :
        fields = line.strip().split(':')

        # If the line is a comment or does not have the required 5 fields, skip it.
        # During a dry run we print why it was skipped so the user knows what happened.
        if match or len(fields) != 5:
            if dry_run == "Y":
                if match:
                    print("Skipping comment line")
                else:
                    print("Error: line does not have 5 fields")
            continue

        # Pull the username, password, and name from the fields
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3], fields[2])

        # Split the groups so the user can be added to multiple groups
        groups = fields[4].split(',')

        # Creating the user account
        print("==> Creating account for %s..." % (username))
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos, username)

        # If dry run was selected we just print the command.
        # If not, we actually run it.
        if dry_run == "Y":
            print(cmd)
        else:
            os.system(cmd)

        # Setting the password for the user
        print("==> Setting the password for %s..." % (username))
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password, password, username)

        if dry_run == "Y":
            print(cmd)
        else:
            os.system(cmd)

        # Add the user to groups if any are listed
        for group in groups:
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username, group))
                cmd = "/usr/sbin/adduser %s %s" % (username, group)

                if dry_run == "Y":
                    print(cmd)
                else:
                    os.system(cmd)

if __name__ == '__main__':
    main()
