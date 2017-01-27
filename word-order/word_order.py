import sys
import collections


lines = [line for line in sys.stdin]
word_count = int(lines[0])
words = lines[1:]


index = collections.OrderedDict()

for i, word in enumerate(words):
    index[word] = index[word] + 1 if word in index else 1

distict = len(index)
counts = [str(index.popitem(last=False)[1]) for i in range(distict)]

print(distict)
print(' '.join(counts))
