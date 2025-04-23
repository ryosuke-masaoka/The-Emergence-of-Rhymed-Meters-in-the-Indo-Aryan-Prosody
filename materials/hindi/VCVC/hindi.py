import re
import collections
file = open('dohavali.txt')
out_f = open('dv_result.txt', 'w')
rp = open('dv_rhymepattern.txt', 'w')
rhymepattern = []
counts = []
types = []
rhymepatterns = []
for line in file:
	line = line.lstrip()
	line = line.rstrip()
	if '/' in line:
		line = re.sub('-', '', line)
		line = re.sub('[\.,]', '', line)
		line = re.sub('\s*\/', '/', line)
		line = re.sub('\\\-', '', line)
		line = re.sub('ai', 'E', line)
		line = re.sub('au', 'O', line)
		line = re.sub('_', '', line)
		m_iter = re.finditer('[aeiouāãĕīïĩŏũüūōēẽUAEOR][^aeiouāãĕīïĩŏũüūōēẽUAEOR\s]*[aeiouāãĕīïĩŏũüūōēẽUAEOR][^aeiouāãĕīïĩŏũüūōēẽUAEOR\s]*\s' , line)
		for m in m_iter:
			m.group()
			rhymepattern.append(m.group())
		n = re.search('[aeiouāãĕīïĩŏũüūōēẽUAEOR][^aeiouāãĕīïĩŏũüūōēẽUAEOR\s]*[aeiouāãĕīïĩŏũüūōēẽUAEOR][^aeiouāãĕīïĩŏũüūōēẽUAEOR\s]*\/$' , line)
		if n:
			odd = n.group()
			odd = re.sub('\/', '', odd)
		o = re.search('[aeiouāãĕīïĩŏũüūōēẽUAEOR][^aeiouāãĕīïĩŏũüūōēẽUAEOR\s]*[aeiouāãĕīïĩŏũüūōēẽUAEOR][^aeiouāãĕīïĩŏũüūōēẽUAEOR\s]*\/\s' , line)
		if o:
			odd = o.group()
			odd = re.sub('\/', '', odd)
			odd = re.sub('\s', '', odd)
		p = re.search('[aeiouāãĕīïĩŏũüūōēẽUAEOR][^aeiouāãĕīïĩŏũüūōēẽUAEOR\s]*[aeiouāãĕīïĩŏũüūōēẽUAEOR][^aeiouāãĕīïĩŏũüūōēẽUAEOR\s]*\/\/' , line)
		if p:
			even = p.group()
			even = re.sub('\/', '', even)
			if even == odd:
				rhymepattern.append(odd)
			else:
				rhymepattern.append(odd)
				rhymepattern.append(even)
for rhyme in rhymepattern:
	rhyme = rhyme.lstrip()
	rhyme = rhyme.rstrip()
	rhyme = re.sub('ï', 'i', rhyme)
	rhyme = re.sub('ü', 'u', rhyme)
	rhyme = re.sub('m$', 'ṁ', rhyme)
	rhyme = re.sub('…', '', rhyme)
	rhyme = re.sub('\]', '', rhyme)
	rhyme = re.sub('E', 'ai', rhyme)
	rhyme = re.sub('O', 'au', rhyme)
	rhyme = re.sub('\/', '', rhyme)
	rhyme = re.sub('R', 'r̥', rhyme)
	rhyme = re.sub('A', 'ā̃', rhyme)
	rhyme = re.sub('U', 'ū̃', rhyme)
	print(rhyme, file=rp)
	rhymepatterns.append(rhyme)
print('types count', file=out_f)
types = list(set(rhymepatterns))
print(len(types), file=out_f)
sumrhyme = len(rhymepatterns)
print('token count', file=out_f)
print(sumrhyme, file = out_f)
count = collections.Counter(rhymepatterns)
counts = list(count.values())
def sum_of_squares(counts):
	return sum(x**2 for x in counts)
result = sum_of_squares(counts)
sumsq = sumrhyme**2
print('RhMP of DV', file=out_f)
print(int(f"{result}")/sumsq, file = out_f)

