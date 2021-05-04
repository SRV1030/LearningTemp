from django.shortcuts import render
from learnapp.forms import fm1,fm2

def index(request):
    context={'text':'Welcome!!'}
    return render(request,'learnapp\index.html',context)

def details(request):
    form1=fm1()
    form2=fm2()
    if request.method=="POST":
        form1=fm1(request.POST)
        form2=fm2(request.POST)

    if form1.is_valid():
        form1.save(commit=True)
    else: print('Error')

    if form2.is_valid():
        form2.save(commit=True)
        return index(request)
    else: print('Error2')

    return render(request,'learnapp\detail.html',{
    'form1':form1,'form2':form2
    })
# Create your views here.
