import re
import collections
file = open('sb.txt')
out_f = open('sb_result.txt', 'w')
rp = open('sb_rhymepattern.txt', 'w')
rhymepattern = []
counts = []
types = []
for line in file:
	line = line.lstrip()
	line = line.rstrip()
	#line = re.sub('\/.*', '', line)
	line = re.sub('-', '', line)
	m_iter = re.finditer('[aeiouāãĕīïĩŏũüūōē][^aeiouāãĕīïĩŏũüūōē\s]*[aeiouāãĕīïĩŏũüūōē][^aeiouāãĕīïĩŏũüūōē]*\s' , line)
	for m in m_iter:
		m.group()
		rhymepattern.append(m.group())
	n = re.search('[aeiouāãĕīïĩŏũüūōē][^aeiouāãĕīïĩŏũüūōē\s]*[aeiouāãĕīïĩŏũüūōē][^aeiouāãĕīïĩŏũüūōē\s]*$' , line)
	if n:
		rhymepattern.append(n.group())
for rhyme in rhymepattern:
	rhyme = rhyme.lstrip()
	rhyme = rhyme.rstrip()
	rhyme = re.sub('ï', 'i', rhyme)
	rhyme = re.sub('ü', 'u', rhyme)
	print(rhyme, file=rp)
print('types count', file=out_f)
types = list(set(rhymepattern))
print(len(types), file=out_f)
sumrhyme = len(rhymepattern)
print('token count', file=out_f)
print(sumrhyme, file = out_f)
count = collections.Counter(rhymepattern)
counts = list(count.values())
def sum_of_squares(counts):
	return sum(x**2 for x in counts)
result = sum_of_squares(counts)
sumsq = sumrhyme**2
print('RhMP of SB', file=out_f)
print(int(f"{result}")/sumsq, file = out_f)

