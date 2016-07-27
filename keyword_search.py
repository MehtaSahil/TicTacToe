# usage : python __file__ "term1" "term2" ... "termN"

import os
from subprocess import call
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
call(bashcommand, shell = True)
call("vim %s" % filename, shell = True)
call("rm %s" % filename, shell = True)
