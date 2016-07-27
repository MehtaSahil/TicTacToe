# usage : python __file__ "term1" "term2" ... "termN"

import os
import sys

command_line_arguments = sys.argv[1:]

# setup params
searchterm = "|".join(command_line_arguments).replace(" ", "")

include = "*.py"
exclude = os.path.basename(__file__)
filename = "%s_find.txt" % "_".join(command_line_arguments).replace(" ", "")

# construct bash command
bashcommand = "grep -Ern '%s' --include '%s' --exclude '%s' > '%s'" % (searchterm, include, exclude, filename)

# execute bash command
os.system(bashcommand)
os.system("vim %s" % filename)
os.system("rm %s" % filename)
