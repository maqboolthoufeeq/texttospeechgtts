from django.shortcuts import render,redirect
from django.http import HttpResponse
import pyttsx3
from gtts import gTTS

# Create your views here.



def index(request):

    return render(request,'generator/index.html')

def checker(request):
    if request.method=='GET':
        innum = request.GET['inputtext']
        num_words = 0
        words = innum.split(" ")
        num_words += len(words)
        print("Number of words:")
        print(num_words)
        if(num_words>1000):
                flag = 'Sorry!!! Word Limit is 1000. You have used '+ str(num_words)+' words'
                return render(request,'generator/index.html', {'flag': flag})
        else:
               
                filen=gTTS(text=innum,lang='en')
                filename='static/temp.mp3'
                filen.save(filename)
                flag2= True
                
                return render(request, 'generator/index.html', {'flag2': flag2})
                