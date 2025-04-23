import re
file = open('sblist2.txt')
out_f = open('sb_gl2.txt', 'w')
gllist = open('sb_gllist.txt', 'w')
numlist = []
number = 0
account = 0
for line in file:
	line = line.lstrip()
	line = line.rstrip()
	num, rp = line.split(' ')
	m = re.match('[aeiouāãĕīïĩŏũüūōē][^aeiouāãĕīïĩŏũüūōē\s]{2,}[aiuãĕïĩŏũü]', rp)
	n = re.match('[eoāīūōē][^aeiouāãĕīïĩŏũüūōē\s]{0,1}[aiuãĕïĩŏũü]', rp)
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
print('RhMP of SB', file=out_f)
print(int(f"{result}")/sumsq, file=out_f)