import sys

sys.path.append("/home/basa/sinling/Sinling")

from sinling import word_splitter

filepath = "new.txt"
a = {}
b= {}
with open(filepath, encoding="utf8") as fp:
    for line in fp:
        x = line.strip().split(' ')

        for j in x:
            a[j]=0

for i in a:
    results = word_splitter.split(i)
    b[results['base']]=0
    
f = open('roots.txt', 'w', encoding="utf8")
#print (a)
for i in b:
    
    f.write(i+ "\n")
    #print (results)

f.close()    
#word = "බළ්ලාට"
#results = word_splitter.split(word)
#print (results['base'])
