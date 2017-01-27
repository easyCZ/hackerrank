import sys
import collections


lines = [line for line in sys.stdin]
word_count = int(lines[0])
words = lines[1:]


index = collections.OrderedDict()

for i, word in enumerate(words):
    if word in index:
        index[word] += 1
    else:
        index[word] = 1

print(len(index))

counts = [str(index.popitem(last=False)[1]) for i in range(len(index))]
# print(counts)
print(' '.join(counts))
