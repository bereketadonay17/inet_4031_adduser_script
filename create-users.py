#!/usr/bin/python3
#!/usr/bin/python3

# INET4031
# Adonay Bereket
# Data Created
# Date Last Modified

#identify what each of these imports is for.
# os is used to run the os commands.
# re is used to load regular expressions (regex.) More specifically, it allows me to search for, match, and manipulate strings based on patterns.
# import sys loads the sys module, providing access to variables and functions.
import os
import re
import sys

#YOUR CODE SHOULD HAVE NONE OF THE INSTRUCTORS COMMENTS REMAINING WHEN YOU ARE FINISHED
#PLEASE REPLACE INSTRUCTOR "PROMPTS" WITH COMMENTS OF YOUR OWN

def main():
    for line in sys.stdin:

        # It's matching with the character "#" that's used for comments like this.
        match = re.match("^#",line)

        # This line removes all the whitespace characters from the beginning to the end of the string. The strip method breaks the cleaned string into a list of substrings wherever it sees a colon.
        fields = line.strip().split(':')

        # If it's a comment or if it does not equal 5 characters.
        # The script skips this line and there won't be an account creation.
        # Because match checks for a comment and fields split the line, the script can check if it has 5 fields.
        # To make sure it's not a comment and that it has the required 5 fields.
        if match or len(fields) != 5:
            continue

        # Pulls the username, passwd, and name from the list and formats the structure.
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3],fields[2])

        # Splits the group field into a list so it can be looped through later.
        groups = fields[4].split(',')

        # Prints a message showing an account is being created.
        print("==> Creating account for %s..." % (username))
        # Builds the adduser command that will create the user account.
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)
        print(cmd)
        os.system(cmd)

        # Prints a message showing that the password is being set.
        print("==> Setting the password for %s..." % (username))
        # Builds the command that sends the password to the passwd command to set the user's password.
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)
        print(cmd)
        os.system(cmd)

        for group in groups:
            # Checks if the group is not "-" meaning the user should be added to that group
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username,group))
                cmd = "/usr/sbin/adduser %s %s" % (username,group)
                print(cmd)
                os.system(cmd)

if __name__ == '__main__':
    main()

