pos_word = []
neg_word = []

Gen1_word = []
Gen2_word = []

Gen1_pos_word = []
Gen1_neg_word = []

Gen2_pos_word = []
Gen2_neg_word = []


print(' input 2 Genre to compare')

Genre1 = input('input Genre1 : ')
Genre2 = input('input Genre2 : ')

with open('word_list/positive-words.txt', 'r',encoding='UTF8') as f:
    posw = f.read()
    pos_word = posw.splitlines()

with open('word_list/negative-words.txt', 'r',encoding='UTF8') as f:
    negw = f.read()
    neg_word = negw.splitlines()


with open(Genre1+'_out\\'+Genre1+'.txt', 'r',encoding='UTF8') as f:
    word1 = f.read()
    Gen1_word = word1.splitlines()

with open(Genre2+'_out\\'+Genre2+'.txt', 'r',encoding='UTF8') as f:
    word2 = f.read()
    Gen2_word = word2.splitlines()


for w in range(len(Gen1_word)):
    if Gen1_word[w].split(',')[0] in pos_word:
        Gen1_pos_word.append(Gen1_word[w])

for w in range(len(Gen1_word)):
    if Gen1_word[w].split(',')[0] in neg_word:
        Gen1_neg_word.append(Gen1_word[w])

for w in range(len(Gen2_word)):
    if Gen2_word[w].split(',')[0] in pos_word:
        Gen2_pos_word.append(Gen2_word[w])

for w in range(len(Gen2_word)):
    if Gen2_word[w].split(',')[0] in neg_word:
        Gen2_neg_word.append(Gen2_word[w])

with open(Genre1+'_out\\'+Genre1+'_pos.txt', 'w',encoding='UTF8') as f:
    for w in Gen1_pos_word[:len(Gen1_pos_word)]:
        f.write("%s" % (w)+"\n")

with open(Genre1+'_out\\'+Genre1+'_neg.txt', 'w',encoding='UTF8') as f:
    for w in Gen1_neg_word[:len(Gen1_neg_word)]:
        f.write("%s" % (w)+"\n")


with open(Genre2+'_out\\'+Genre2+'_pos.txt', 'w',encoding='UTF8') as f:
    for w in Gen2_pos_word[:len(Gen2_pos_word)]:
        f.write("%s" % (w)+"\n")

with open(Genre2+'_out\\'+Genre2+'_neg.txt', 'w',encoding='UTF8') as f:
    for w in Gen2_neg_word[:len(Gen2_neg_word)]:
        f.write("%s" % (w)+"\n")