from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):

	return render(request,'home.html')
def count(request):
        fulltext=request.GET['fulltext']
        wordlist=fulltext.split()
        worddic={}
        for i in wordlist:
            if wordlist.count(i)>=2:
                worddic[i]+=1
            else:
                worddic[i]=1
        #return render(request,'count.html',{'fulltext':fulltext,'count':len(wordlist)})
        return render(request,'count.html',{'fulltext':fulltext,'worddic':worddic,'count':len(wordlist)})
        

