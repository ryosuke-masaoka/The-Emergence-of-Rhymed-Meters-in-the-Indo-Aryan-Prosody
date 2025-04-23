import re
import collections
file = open('pd.txt')
out_f = open('pd_result.txt', 'w')
rp = open('pd_rhymepattern.txt', 'w')
rp_types = open('pd_types.txt', 'w')
rhymepattern = []
counts = []
types = []
endrhyme = []
rhymepatterns = []
linenum = 0
for line in file:
	linenum += 1
	line = line.lstrip()
	line = line.rstrip()
	line = re.sub('[0123456789\{\},\._\']', '', line)
	line = re.sub('/', '', line)
	line = re.sub('-', '', line)
	line = line.rstrip()
	m_iter = re.finditer('[aeiouāãĕīïĩŏũüūōēẽ][^aeiouāãĕīïĩŏũüūōēẽ\s]*[aeiouāãĕīïĩŏũüūōēẽ][^aeiouāãĕīïĩŏũüūōēẽ$]*\s' , line)
	for m in m_iter:
		mrhyme = m.group()
		mrhyme = mrhyme.rstrip()
		rhymepattern.append(mrhyme)
	n = re.search('[aeiouāãĕīïĩŏũüūōēẽ][^aeiouāãĕīïĩŏũüūōēẽ\s]*[aeiouāãĕīïĩŏũüūōēẽ][^aeiouāãĕīïĩŏũüūōēẽ\s]*$' , line)
	if n:
		endrhyme.append(n.group())
	if linenum % 3 == 2:
		erset = list(set(endrhyme))
		for er in erset:
			rhymepattern.append(er)
		endrhyme = []
for rhyme in rhymepattern:
	rhyme = rhyme.lstrip()
	rhyme = rhyme.rstrip()
	rhyme = re.sub('ï', 'i', rhyme)
	rhyme = re.sub('ü', 'u', rhyme)
	rhyme = re.sub('[0-9]', '', rhyme)
	rhyme = re.sub(r'\$', '', rhyme)
	rhyme = re.sub('$', '', rhyme)
	rhyme = re.sub('\s', '', rhyme)
	print(rhyme, file=rp)
	rhymepatterns.append(rhyme)
print('types count', file=out_f)
types = list(set(rhymepatterns))
print(len(types), file=out_f)
for type in types:
	print(type, file=rp_types)
sumrhyme = len(rhymepatterns)
print('token count', file=out_f)
print(sumrhyme, file = out_f)
count = collections.Counter(rhymepatterns)
counts = list(count.values())
def sum_of_squares(counts):
	return sum(x**2 for x in counts)
result = sum_of_squares(counts)
sumsq = sumrhyme**2
print('RhMP of PD', file=out_f)
print(int(f"{result}")/sumsq, file = out_f)

