from os import listdir
from os.path import isfile, join
import re

pos_word = []
neg_word = []

fam_word = []
cri_word = []

fam_pos_word = []
fam_neg_word = []

cri_pos_word = []
cri_neg_word = []


with open('word_list/positive-words.txt', 'r',encoding='UTF8') as f:
    posw = f.read()
    pos_word = posw.splitlines()

with open('word_list/negative-words.txt', 'r',encoding='UTF8') as f:
    negw = f.read()
    neg_word = negw.splitlines()


with open('Crime_out/Crime.txt', 'r',encoding='UTF8') as f:
    cword = f.read()
    cri_word = cword.splitlines()

with open('Family_out/Family.txt', 'r',encoding='UTF8') as f:
    fword = f.read()
    fam_word = fword.splitlines()


for w in range(len(fam_word)):
    if fam_word[w].split(',')[0] in pos_word:
        fam_pos_word.append(fam_word[w])

for w in range(len(fam_word)):
    if fam_word[w].split(',')[0] in neg_word:
        fam_neg_word.append(fam_word[w])

for w in range(len(cri_word)):
    if cri_word[w].split(',')[0] in pos_word:
        cri_pos_word.append(cri_word[w])

for w in range(len(cri_word)):
    if cri_word[w].split(',')[0] in neg_word:
        cri_neg_word.append(cri_word[w])

with open('Family_out/Family_pos.txt', 'w',encoding='UTF8') as f:
    for w in fam_pos_word[:len(fam_pos_word)]:
        f.write("%s" % (w)+"\n")

with open('Family_out/Family_neg.txt', 'w',encoding='UTF8') as f:
    for w in fam_neg_word[:len(fam_neg_word)]:
        f.write("%s" % (w)+"\n")

with open('Crime_out/Crime_pos.txt', 'w',encoding='UTF8') as f:
    for w in cri_pos_word[:len(cri_pos_word)]:
        f.write("%s" % (w)+"\n")

with open('Crime_out/Crime_neg.txt', 'w',encoding='UTF8') as f:
    for w in cri_neg_word[:len(cri_neg_word)]:
        f.write("%s" % (w)+"\n")