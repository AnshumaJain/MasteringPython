
import sys

print sys.argv


if sys.argv[1] == "w":
	print "move forward"
elif sys.argv[1] == "s":
	print "move right"
else:
	print "undefined"
