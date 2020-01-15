#!/usr/bin/env python3
import os, sys

def parsefile(path):
	f = open(path)
	line, spaces, tabs = 0,0,0
	for line, text in enumerate(f):
		spaces = spaces + text.count('')
		tabs = tabs + text.count('\t')
	f.close()
	return spaces, tabs, line

def main(path):
	if os.path.exists(path):
		spaces,tabs,line = parsefile(path)
		print('spaces {} tabs {} line {}'.format(spaces,tabs,line+1))
		return True
	else:
		return False


if len(sys.argv)>1:
	main(sys.argv[1])
else:
	sys.exit(-1)
sys.exit(0)
