from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Value
from django.urls import reverse

def home(request):
    std = Value.objects.all()
    stm = Value.objects.values("trade_code").distinct()
    
   
    
    
   
    
    return render(request,"demofrontend/home.html",{'std':std,'stm':stm})



def moon(request,trade_code):
    
    stm = Value.objects.values("trade_code").distinct()
    # trade_code = request.POST.get("trade_code")
    stf = Value.objects.filter(trade_code = trade_code)
    
    return render(request,"demofrontend/chart.html",{'stf':stf,'stm':stm})



def add(request):
    if request.method=='POST':
        print("added")
        
        date = request.POST.get("date")
        trade_code = request.POST.get("trade_code")
        high = request.POST.get("high")
        low = request.POST.get("low")
        openn = request.POST.get("openn")
        close = request.POST.get("close")
        volume = request.POST.get("volume")
    
        s = Value()
        s.date = date
        s.trade_code = trade_code
        s.high = high
        s.low = low
        s.openn = openn
        s.close = close
        s.volume = volume
        
        s.save()
        
        return redirect("/demofrontend/home/")
    
    # return render(request,"demofrontend/home.html",{})

         

def deletee(request,id):
    
    s = Value.objects.get(id=id)
    s.delete()
    
    # return render(request,"demofrontend/home.html",{})

    return redirect("/demofrontend/home/")

def getupdate(request,id):
    
    moon = Value.objects.get(id=id)
    
    return render(request,"demofrontend/update.html",{'moon':moon})
    
   

   

def addd(request,id):

        
        date = request.POST.get("date")
        trade_code = request.POST.get("trade_code")
        high = request.POST.get("high")
        low = request.POST.get("low")
        openn = request.POST.get("openn")
        close = request.POST.get("close")
        volume = request.POST.get("volume")
    
        s = Value.objects.get(id=id)
        s.date = date
        s.trade_code = trade_code
        s.high = high
        s.low = low
        s.openn = openn
        s.close = close
        s.volume = volume
        
        s.save()
        
        return redirect("/demofrontend/home/")