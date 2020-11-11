import re

import numpy as np

def levenshtein(seq1, seq2):
    size_x = len(seq1) + 1
    size_y = len(seq2) + 1
    matrix = np.zeros ((size_x, size_y))
    for x in xrange(size_x):
        matrix [x, 0] = x
    for y in xrange(size_y):
        matrix [0, y] = y

    for x in xrange(1, size_x):
        for y in xrange(1, size_y):
            if seq1[x-1] == seq2[y-1]:
                matrix [x,y] = min(
                    matrix[x-1, y] + 1,
                    matrix[x-1, y-1],
                    matrix[x, y-1] + 1
                )
            else:
                matrix [x,y] = min(
                    matrix[x-1,y] + 1,
                    matrix[x-1,y-1] + 1,
                    matrix[x,y-1] + 1
                )
    return (matrix[size_x - 1, size_y - 1])



f = file('frq.txt', 'r')

letters_re = re.compile('[a-z]+$')

nogo = set(['fecal', 'dotcom', 'rape', 'moron', 'vagina', 'penis', 'erect', 'negro', 'piss', 'nigger', 'mutilate', 'macho', 'jihad', 'virgin', 'slave', 'cocaine', 'homo', 'junkie', 'anal', 'dick', 'cunt', 'cum', 'nah', 'violate', 'dwarf', 'whore', 'diaper', 'corrupt', 'aha', 'ahem', 'cunt', 'whereas', 'sex', 'orgasm', 'fuck'])

i=0
line = f.readline()

words = []

while(line):
    line = line[:-2]

    length = 3 < len(line) and len(line) <= 8

    
    if length and line not in nogo and letters_re.match(line):
        for w in words:
            m = min(len(w), len(line))
            ok = w[:4] != line[:4] and w[:m] != line[:m]
            

            if not ok:
                #print 'skipping ' + line + ' due to ' + w
                line = None
                break
        if line:
            words.append(line)
            i = i + 1
            if i == 4096:
                break
    line = f.readline()

words.sort(cmp=lambda x, y: -1 if x < y else 1)

for word in words:
    print word

