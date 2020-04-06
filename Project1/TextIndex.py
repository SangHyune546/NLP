import os
import re

from os import listdir
from os.path import isfile, join


stop_word = []
r_word=[]

dic = {}
iter = 1

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)

with open('Stopword/SWord2.txt', 'r',encoding='UTF8') as f:
    sword = f.read()
    stop_word = sword.splitlines()

Uinput = input('input Genre : ')

files = [f for f in listdir(os.getcwd()+'\\'+Uinput) if isfile(join(os.getcwd()+'\\'+Uinput, f))]
print(files,"\n")
print(len(files),"\n")

for name in files:
    with open(Uinput+'\\'+name, 'r',encoding='UTF8') as f:
        text = f.read()       
        words = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]', '', text).split()

    for i in range(0, len(words)):
        words[i] = words[i].lower()

    for word in words:
        if word not in stop_word:
            r_word.append(word)
        else:
            pass

    if r_word in stop_word:
        print(r_word)

    for w in r_word:
        if w in dic:
            dic[w] += 1
        else:
            dic[w] = 1

    r_word.clear()
    words.clear()
    print("Processing",Uinput,"Scripts",iter,"/",len(files))
    iter += 1


lst = sorted(dic.items(), key=lambda kv: kv[1], reverse=True)

print(Uinput + "'s Dictionary length  : ",len(lst))

print("Top 10 words : \n")

for w, c in lst[:10]:
    print(w, c)

createFolder(os.getcwd()+'\\'+Uinput+'_out\\')

with open(Uinput+'_out\\'+Uinput+'.txt', 'w',encoding='UTF8') as f:
    for w,c in lst[:len(lst)]:
        f.write("%s, %d" % (w,c)+"\n")