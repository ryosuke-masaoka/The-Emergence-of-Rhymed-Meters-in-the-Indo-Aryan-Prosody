import re
file = open('rvlist.txt')
out_f = open('rv_gl.txt', 'w')
gllist = open('rv_gllist.txt', 'w')
numlist = []
number = 0
account = 0
for line in file:
	line = line.lstrip()
	line = line.rstrip()
	line = re.sub('r̥̄', '@', line)
	line = re.sub('r̥', 'R', line)
	line = re.sub('l̥', 'L', line)
	line = re.sub('ai', 'E', line)
	line = re.sub('au', 'O', line)
	line = re.sub('l̥̄', '%', line)
	num, rp = line.split(' ')
	m = re.match('[aeiouāīū@RL\%EO][^aeiouāīū@RL\%EO\s]{2,}[aiuRL]', rp)
	n = re.match('[eoāīū@\%EO][^aeiouāīū@RL\%EO\s]{0,1}[aiuRL]', rp)
	if m or n:
		numlist.append(int(num))
		print(rp, file=gllist)
types = len(numlist)
print('types count', file=out_f)
print(types, file=out_f)
token = sum(numlist)
print('token count', file=out_f)
print(token, file=out_f)
def sum_of_squares(numlist):
	return sum(x**2 for x in numlist)
result = sum_of_squares(numlist)
sumsq = token**2
print('RhMP of RV', file=out_f)
print(int(f"{result}")/sumsq, file=out_f)