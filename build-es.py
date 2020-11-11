# -*- coding: utf-8 -*-

import re



f = file('10000_formas.TXT', 'r')

letters_re = re.compile('[a-z]+$')

nogo = set(['sáenz', 'saint', 'rtve', 'ronald', 'psoe', 'kant', 'vizcaya', 'vitoria', 'violación', 'yeltsin', 'tony', 'toreo', 'franquismo', 'press', 'miss', 'cogió', 'mary', 'kong', 'texas', 'soviética', 'smith', 'sida', 'sexos', 'sexual', 'sanz', 'cavallo', 'velasco', 'terrorismo', 'reuter', 'esclavos', 'sainz', 'idiota', 'pene', 'erecto', 'orina', 'heces', 'mutilar', 'macho', 'jihad', 'virgen', 'esclavo', 'cocaina', 'coger', 'concha', 'anal', 'droga', 'semen', 'violate', 'dwarf', 'puta', 'pañal', 'corrupto', 'sexo', 'orgasmo'])

i=0
line = f.readline()

words = []
good = []

pairs = [['á', 'a'], ['é', 'e'], ['í', 'i'], ['ó', 'o'], ['ú', 'u'], ['ü', 'u'], ['ñ', 'n']]

def norm(s):
    for [a, b] in pairs:
        s = s.replace(a, b)
    return s

while(line):
    line = line[8:]

    l = min(line.find(' '), line.find('\t'))

    line = line[:l]

    length = 3 < len(line) and len(line) <= 10

    
    if length and line not in nogo and line.find('ü') < 0 and line.find('ii') < 0 and line.find('xx') < 0 and line.find('ç') < 0 and line not in ['janeiro', 'halla', 'cruyff', 'cesid', 'bonaerense', 'bill', 'urss', 'kennedy', 'chirac', 'clinton']:
        lw = norm(line)
        for w in words:
            m = min(len(w), len(lw))
            ok = w[:6] != lw[:6] and w[:m] != lw[:m] and w != lw
            

            if not ok:
                #print 'skipping ' + line + ' due to ' + w
                line = None
                break
        if line:
            words.append(lw)
            good.append(line)
            i = i + 1
            if i ==4096:
                break
    line = f.readline()

good.sort(cmp=lambda x, y: -1 if norm(x) < norm(y) else 1)

for word in good:
    print word
