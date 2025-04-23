import re
file = open('dvlist.txt')
out_f = open('dv_gl.txt', 'w')
gllist = open('dv_gllist.txt', 'w')
numlist = []
number = 0
account = 0
for line in file:
	line = line.lstrip()
	line = line.rstrip()
	line = re.sub('ai', 'E', line)
	line = re.sub('au', 'O', line)
	num, rp = line.split(' ')
	m = re.match('[aeiouāãĕīïĩŏũüūōēẽUAEOR][^aeiouāãĕīïĩŏũüūōēẽUAEOR\s]{2,}[aiuãĕïĩŏũüẽR]', rp)
	n = re.match('[eoāīūōēUAEO][^aeiouāãĕīïĩŏũüūōēẽUAEOR\s]{0,1}[aiuãĕïĩŏũüẽR]', rp)
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
print('RhMP of DV', file=out_f)
print(int(f"{result}")/sumsq, file=out_f)