import re
file = open('pclist.txt')
out_f = open('pc_gl.txt', 'w')
gllist = open('pc_gllist.txt', 'w')
numlist = []
number = 0
account = 0
for line in file:
	line = line.lstrip()
	line = line.rstrip()
	num, rp = line.split(' ')
	m = re.match('[aeiouāãĕīïĩŏũüūōēẽ][^aeiouāãĕīïĩŏũüūōēẽ\s]{2,}[aiuãĕïĩŏũüẽ]', rp)
	n = re.match('[eoāīūōē][^aeiouāãĕīïĩŏũüūōēẽ\s]{0,1}[aiuãĕïĩŏũüẽ]', rp)
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
print('RhMP of PC', file=out_f)
print(int(f"{result}")/sumsq, file=out_f)