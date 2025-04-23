import re
import collections
file = open('rv.txt')
out_f = open('rv_result.txt', 'w')
rp = open('rv_rhymepattern.txt', 'w')
rhymepattern = []
counts = []
types = []
rhymepatterns = []
for line in file:
	line = line.lstrip()
	line = line.rstrip()
	line = re.sub('r̥̄', '@', line)
	line = re.sub('r̥', 'R', line)
	line = re.sub('l̥', 'L', line)
	line = re.sub('ai', 'E', line)
	line = re.sub('au', 'O', line)
	line = re.sub('l̥̄', '%', line)
	m_iter = re.finditer('[aeiouāīū@RL\%EO][^aeiouāīū@RL\%EO\s]*[aeiouāīū@RL\%EO][^aeiouāīū@RL\%EO\s]*[aeiouāīū@RL\%EO][^aeiouāīū@RL\%EO\s]*\s' , line)
	for m in m_iter:
		m.group()
		rhymepattern.append(m.group())
	n = re.search('[aeiouāīū@RL\%EO][^aeiouāīū@RL\%EO\s]*[aeiouāīū@RL\%EO][^aeiouāīū@RL\%EO\s]*[aeiouāīū@RL\%EO][^aeiouāīū@RL\%EO\s]*$' , line)
	if n:
		rhymepattern.append(n.group())
for rhyme in rhymepattern:
	rhyme = rhyme.lstrip()
	rhyme = rhyme.rstrip()
	rhyme = re.sub('@', 'r̥̄', rhyme)
	rhyme = re.sub('R', 'r̥', rhyme)
	rhyme = re.sub('L', 'l̥', rhyme)
	rhyme = re.sub('E', 'ai', rhyme)
	rhyme = re.sub('O', 'au', rhyme)
	rhyme = re.sub('\%', 'l̥̄', rhyme)
	rhyme = re.sub(r'r$', 'ḥ', rhyme)
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
print('RhMP of RV', file=out_f)
print(int(f"{result}")/sumsq, file = out_f)

