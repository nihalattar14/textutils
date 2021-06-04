from django.http import HttpResponse
from django.shortcuts import render

def index(request):

    return render(request,'index.html')

def analyze(request):

    # GET the text
    djtext = request.GET.get('text','default')

    #checkbox values

    removepunc = request.GET.get('removepunc','off')
    fullcaps = request.GET.get('fullcaps','off')
    newlineremover = request.GET.get('newlineremover','off')
    extraspaceremover = request.GET.get('extraspaceremover','off')
    charcount = request.GET.get('charcount','off')


    #check with checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'Purpose':'Removed Punctuations','analyzed_text':analyzed}
        #Analyze the text
        return render(request, 'analyze.html', params)

    elif(fullcaps == 'on'):
        analyzed = djtext.upper()
        params = {'Purpose': 'Changed to Upper case', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif(newlineremover == 'on'):
        analyzed = ""
        for char in djtext:
            if char != "\n":
                analyzed = analyzed + char
        params = {'Purpose': 'Remove New Lines ', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif(extraspaceremover == 'on'):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
              analyzed = analyzed + char

        params = {'Purpose': 'Changed to Upper case', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif(charcount == 'on'):
        analyzed = 0
        for i in range(0, len(djtext)):
            if(djtext[i]!=''):
                analyzed = analyzed + 1
        params = {'Purpose': 'Changed to Upper case', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)


    else:
        return HttpResponse("Please Select atleast any one checkbox")



# def removepunc(request):
#
#     # GET the text
#     djtext = request.GET.get('text','default')
#     print(djtext)
#     #Analyze the text
#     return HttpResponse("remove punc")
#
# def capfirst(request):
#     return HttpResponse("capitalize first")
#
# def newlineremove(request):
#     return HttpResponse("newline remove")
#
# def spaceremove(request):
#     return HttpResponse("space remove<a href = '/'>Back</a>")
#
# def charcount(request):
#     return HttpResponse("char count")