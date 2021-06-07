from django.http import HttpResponse
from django.shortcuts import render

def index(request):

    return render(request,'index.html')

def analyze(request):

    # GET the text
    djtext = request.POST.get('text','default')

    #checkbox values

    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')
    charcount = request.POST.get('charcount','off')

    params = {}


    #check with checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'Purpose':'Removed Punctuations','analyzed_text':analyzed}
        djtext = analyzed
        #Analyze the text
        # return render(request, 'analyze.html', params)

    if(fullcaps == 'on'):
        analyzed = djtext.upper()
        params = {'Purpose': 'Changed to Upper case', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if(newlineremover == 'on'):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'Purpose': 'Remove New Lines ', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if(extraspaceremover == 'on'):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
              analyzed = analyzed + char

        params = {'Purpose': 'Changed to Upper case', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if(charcount == 'on'):
        analyzed = 0
        for i in range(0, len(djtext)):
            if(djtext[i]!=''):
                analyzed = analyzed + 1
        params = {'Purpose': 'Changed to Upper case', 'analyzed_text': analyzed}
        # return render(request, 'analyze.html', params)

    if(removepunc!="on" and fullcaps!="on" and newlineremover!="on" and extraspaceremover!="on" and charcount!="on"):
        return HttpResponse("Please select atleast one operation ")

    return render(request, 'analyze.html', params)


