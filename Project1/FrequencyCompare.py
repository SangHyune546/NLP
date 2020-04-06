import os

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)

srcTxt = input('input Source Genre : ')
cmpTxt = input('input Compare Genre : ')
Feature = input('input Feature pos or neg : ')

src_word = []
cmp_word = []

cmp_result = []


with open('D:\\NLP\\Project1\\'+srcTxt+'_out\\'+srcTxt+'_'+Feature+'.txt', 'r',encoding='UTF8') as f:
    srcw = f.read()
    src_word = srcw.splitlines()

with open('D:\\NLP\\Project1\\'+cmpTxt+'_out\\'+cmpTxt+'_'+Feature+'.txt', 'r',encoding='UTF8') as f:
    cmpw = f.read()
    cmp_word = cmpw.splitlines()

print(srcTxt+' : ',src_word[:10])
print(cmpTxt+' : ',cmp_word[:10])

createFolder('D:\\NLP\\Project1\\'+srcTxt+'_'+cmpTxt+'_'+Feature)

with open('D:\\NLP\\Project1\\'+srcTxt+'_'+cmpTxt+'_'+Feature+'\\'+srcTxt+cmpTxt+'_'+Feature+'_'+'out.txt', 'w',encoding='UTF8') as f:
    f.write("word,"+cmpTxt+","+srcTxt+","+ "\n")
    for w in range(len(cmp_word)):
        for c in range(len(src_word)):
            if cmp_word[w].split(',')[0] == src_word[c].split(',')[0]:
                f.write("%s, %s, %s" % (cmp_word[w].split(',')[0],cmp_word[w].split(',')[1],src_word[c].split(',')[1])+"\n")
    

