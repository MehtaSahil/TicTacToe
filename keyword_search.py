import os

# setup params
print "enter search term (only one)"
searchterm = str(raw_input())
include = "*.py"
exclude = os.path.basename(__file__)
filename = "%s_find.txt" % searchterm

# construct bash command
bashcommand = "grep -Ern '%s' --include '%s' --exclude '%s' > '%s'" % (searchterm, include, exclude, filename)

# execute bash command
os.system(bashcommand)
os.system("vim %s" % filename)
os.system("rm %s" % filename)
