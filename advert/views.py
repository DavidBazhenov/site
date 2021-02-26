
from django.shortcuts import render

def advert_list(request,*args,**kwargs):
	return render(request,'advert/html/advert.html',{})
def datascientist(request,*args,**kwargs):
	return render(request,'advert/html/datascientist.html',{})
def pythonrazrabotchik(request,*args,**kwargs):
	return render(request,'advert/html/pythonrazrabotchik.html',{})
def veb_razrabotchik(request,*args,**kwargs):
	return render(request,'advert/html/veb_razrabotchik.html',{})
def testirovchik(request,*args,**kwargs):
	return render(request,'advert/html/testirovchik.html',{})
def Java(request,*args,**kwargs): 
	return render(request,'advert/html/Java.html',{})