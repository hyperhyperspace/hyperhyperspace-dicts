import sys
import locale

ws = file(sys.argv[1], 'r')

i = 0

lines = map(lambda x: x[:-1], ws.readlines())

s = "["
first = True
for line in lines:
	if not first:
		s = s + ","
	first = False
	s = s + "'" + line + "'"
s = s + "]"

print s



