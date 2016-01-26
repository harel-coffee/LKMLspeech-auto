#txt= "Mr. Green killed Colonel Mustard in the study with the candlestick. Mr. Green is not a very nice fellow";
#sentences=nltk.tokenize.sent_tokenize(txt)
#tokens = [nltk.tokenize.word_tokenize (s) for s in sentences]
#pos_tagged_tokens=[nltk.pos_tag (t) for t in tokens]

import os
import operator
from sklearn import preprocessing
import nltk

negCorpus=[]
posCorpus=[]
partsOfSpeechTagsGuideDict={}

with open(os.path.join("C:\Users\danie_000\Documents\Elon\Big Honors Project of Death\Python\Classifier", "summaryOfPOSTags.txt")) as fh:
    content = fh.readlines()
    for line in content:
        splitLine=line.split("\t")
        partsOfSpeechTagsGuideDict[splitLine[1]]=splitLine[2].strip()

inDir='C:/Users/danie_000/Documents/Elon/Big Honors Project of Death/Data/linusMoreStripping3/'
for filename in os.listdir(inDir):
    with open(os.path.join(inDir, filename)) as fh:
        contents = fh.read()
        contents=contents.lower()
        contents=contents.replace("linus","")
        contents= contents.replace("torvalds","")
        xsToRemove="xx"
        for i in range (2,20):
            contents= contents.replace(xsToRemove,"")
            xsToRemove=xsToRemove+"x"
        negCorpus.append(contents)
print "FINISHED LINUS"

inDir='C:/Users/danie_000/Documents/Elon/Big Honors Project of Death/Data/gregMoreStripping3/'
for filename in os.listdir(inDir):
    with open(os.path.join(inDir, filename)) as fh:
        contents = fh.read()
        contents=contents.lower()
        contents=contents.replace("greg","")
        contents= contents.replace("hartman","")
        contents= contents.replace("kroah","")
        contents= contents.replace("kh","")
        xsToRemove="xx"
        for i in range (2,20):
            contents= contents.replace(xsToRemove,"")
            xsToRemove=xsToRemove+"x"
        posCorpus.append(contents)

partsofspeechDictLinus={}
partsofspeechDictGreg={}

for doc in negCorpus:
    try:
        sentences=nltk.tokenize.sent_tokenize(doc)
        tokens = [nltk.tokenize.word_tokenize (s) for s in sentences]
        pos_linus_tagged_tokens=[nltk.pos_tag (t) for t in tokens]
        
        for sentence in pos_linus_tagged_tokens:
            for posTag in sentence:
                if posTag[1] in partsofspeechDictLinus.keys():
                    partsofspeechDictLinus[posTag[1]]=partsofspeechDictLinus[posTag[1]]+1
                else:
                    partsofspeechDictLinus[posTag[1]]=0
    except:
        pass

totalCountOfTermsLinus=0
for tag,numTag in partsofspeechDictLinus.iteritems():
    if tag in partsOfSpeechTagsGuideDict.keys():
        print partsOfSpeechTagsGuideDict[tag],"|",str(numTag)
    else: 
        print tag,"|",str(numTag)
    totalCountOfTermsLinus=totalCountOfTermsLinus+numTag
print "Total Number of Terms for Linus: ", totalCountOfTermsLinus
     
           
for doc in posCorpus:
    try:
        sentences=nltk.tokenize.sent_tokenize(doc)
        tokens = [nltk.tokenize.word_tokenize (s) for s in sentences]
        pos_greg_tagged_tokens=[nltk.pos_tag (t) for t in tokens]
        
        for sentence in pos_greg_tagged_tokens:
            for posTag in sentence:
                if posTag[1] in partsofspeechDictGreg.keys():
                    partsofspeechDictGreg[posTag[1]]=partsofspeechDictGreg[posTag[1]]+1
                else:
                    partsofspeechDictGreg[posTag[1]]=0
    except:
        pass
        
totalCountOfTermsGreg=0  
for tag,numTag in partsofspeechDictGreg.iteritems():
    if tag in partsOfSpeechTagsGuideDict.keys():
        print partsOfSpeechTagsGuideDict[tag],"|",str(numTag)
    else: 
        print tag,"|",str(numTag)
    totalCountOfTermsGreg=totalCountOfTermsGreg+numTag
print "Total Number of Terms for Greg: ",totalCountOfTermsGreg
