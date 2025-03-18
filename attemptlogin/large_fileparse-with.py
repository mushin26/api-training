#!/usr/bin/python3

# parse keystone.common.wsgi and return number of failed login attempts
loginfail = 0 # counter for fails
post = 0
list_ip = []
# open the file for reading
with open("/home/student/mycode/attemptlogin/keystone.common.wsgi") as kfile:

    # loop over the file
    for line in kfile:
        # if this 'fail pattern' appears in the line...
        if "- - - - -] Authorization failed" in line:
            loginfail += 1 # this is the same as loginfail = loginfail + 1
            list_ip.append(line.split()[-1])
        if  "POST" in line:
            post += 1    




print("The number of failed log in attempts is", loginfail)
print("The number of POST operation in log is", post)
print ("The IP list problematique is "list_ip)
