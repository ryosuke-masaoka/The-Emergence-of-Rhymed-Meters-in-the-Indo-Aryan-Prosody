import re
import collections
file = open('ss.txt')
out_f = open('ss_result.txt', 'w')
rp = open('ss_rhymepattern.txt', 'w')
rhymepattern = []
counts = []
types = []
rhymepatterns = []
for line in file:
	line = line.lstrip()
	line = line.rstrip()
	line = re.sub('\/.*', '', line)
	line = re.sub('\'\s', 'a ', line)
	line = re.sub('\.', '', line)
	line = re.sub('-', '', line)
	m_iter = re.finditer('[aeiouāãĕīïĩŏũüūōēeo][^aeiouāãĕīïĩŏũüūōēeo\s]*[aeiouāãĕīïĩŏũüūōēeo][^aeiouāãĕīïĩŏũüūōēeo\s]*[aeiouāãĕīïĩŏũüūōēeo][^aeiouāãĕīïĩŏũüūōēeo]*\s' , line)
	for m in m_iter:
		m.group()
		rhymepattern.append(m.group())
	n = re.search('[aeiouāãĕīïĩŏũüūōēeo][^aeiouāãĕīïĩŏũüūōēeo\s]*[aeiouāãĕīïĩŏũüūōēeo][^aeiouāãĕīïĩŏũüūōēeo\s]*[aeiouāãĕīïĩŏũüūōēeo][^aeiouāãĕīïĩŏũüūōēeo\s]*$' , line)
	if n:
		rhymepattern.append(n.group())
for rhyme in rhymepattern:
	rhyme = rhyme.lstrip()
	rhyme = rhyme.rstrip()
	rhyme = re.sub('ï', 'i', rhyme)
	rhyme = re.sub('ü', 'u', rhyme)
	rhyme = re.sub('m$', 'ṁ', rhyme)
	rhyme = re.sub('…', '', rhyme)
	rhyme = re.sub('\]', '', rhyme)
# when you replace e an o in closed syllables with i and u, please apply two lines below
	#rhyme = re.sub(r'[eēĕ](?=[^aeiouāãĕīïĩŏũüūōēeo\s]*)', 'i', rhyme)
	#rhyme = re.sub(r'[oōŏ](?=[^aeiouāãĕīïĩŏũüūōēeo\s]*)', 'u', rhyme)
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
print('RhMP of SS', file=out_f)
print(int(f"{result}")/sumsq, file = out_f)

