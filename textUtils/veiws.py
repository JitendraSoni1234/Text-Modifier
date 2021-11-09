from django.http import HttpResponse

from django.shortcuts import render
def index(request):
    return render(request,'index.htm')

def analyze(request):
    djtext = request.POST.get('text','default')
    removepunc = request.POST.get('removepunc','off')
    capfull = request.POST.get('capfull','off')
    removeNewLine = request.POST.get('removeNewLine','off')
    spaceRemover = request.POST.get('spaceRemover','off')
    charCount = request.POST.get('charCount','off')
    analyzed = ""

    if removepunc == 'on':
        analyzed = ""
        puncutations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        for char in djtext:
            if char not in puncutations:
                analyzed += char
        parms = {'purpose': 'remove puncations', 'analyzed_text': analyzed}
        djtext = analyzed
    if capfull ==  'on':
        analyzed = ""
        for char in djtext:
            analyzed += char.upper()
        parms = {'purpose': 'remove puncations', 'analyzed_text': analyzed}
        djtext = analyzed

    if removeNewLine ==  'on':
        analyzed = ""
        for char in djtext:
            if char !="\n" and char != "\r":
                analyzed += char
        parms = {'purpose': 'remove puncations', 'analyzed_text': analyzed}
        djtext = analyzed

    if spaceRemover == 'on':
        analyzed = ""
        for char in djtext:
            if char not in "  ":
                analyzed += char
        parms = {'purpose': 'remove puncations', 'analyzed_text': analyzed}
        djtext = analyzed

    else:
        analyzed = djtext


    parms = {'purpose': 'remove puncations', 'analyzed_text': analyzed}
    return render(request,'analyzed.htm',parms)

# def capfirst(request):
#
#
# def newlineremover(request):
#
#
# def spaceremover(request):
#
#
# def charcount(request):
#
