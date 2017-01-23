#imports
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from django.http import HttpResponseRedirect
from django.http import HttpResponse
import os
from time import sleep
from random import randint
import sys 
import requests
import re
# Create your views here.
def index(request):
	
	return render(request,'Index.html')

def booking(request):
	return render(request,'Booking.html')
	
def currency(request):
	return render(request,'Currency.html')

def gallery(request):
	return render(request,'Gallery.html')
def rpg(request):
	
	inventory = {
		'exp':1,
	   'logs':0
	}
	return render(request,'rpg.html',inventory)
def formulas(request):
	form = NameForm(request.POST)
	
	context= {
	'distance': form.data,
	#'timetaken': form.data['timetaken'],
	#'mass': form.data['mass'],
	#'gforce': form.data['gforce'],
	'form':form,
	}
		
	return render(request, 'formulas.html',context)
	

	
def findweight(m,g):
    d={'weight':m*g,'mass':m,'gForce':g}
     
   
    print "Your mass is", m
    print "The gravitational force is", g
    #Earth gravitational field strenghth is 9.8m/s
    print "Your weight is", m*g
    return d

def speedcalc(d,t):
    dct={"distance":d,"timetaken":t,"speed":d/t}
    
    print "Speed calculator"
    print "Distance covered: ", d
    print "Time taken: ", t
    print d/t, "m/s"
    return dct

	
def portfolio(request):
	data=requests.get('https://github.com/nandopatel').content
	soup=BeautifulSoup(data)
	resp=soup.findAll('h2', {"class":"f4 text-normal mb-2"})[0]
	contributions=re.findall('>.*<',str(resp),re.DOTALL)[0].replace('>','').replace('<','')


	lst=soup.findAll('div',{"class":"js-calendar-graph is-graph-loading graph-canvas calendar-graph height-full"})

	cal=re.sub(r'(>)(.*?</text>)',r'align=center fill=grey\1\2',str(lst[0]))
	

	return render(request,'portfolio.html',{'calender':cal,'contributions':contributions})


from .forms import speedandweightForm

def feedback(request):
    if request.method == "POST":
		#form = speedandweightForm(request.POST)
		d=float(request.POST.get('distance_travelled'))
		t=float(request.POST.get('time'))
		m=float(request.POST.get('mass'))
		g=float(request.POST.get('Gravitational_Force'))
		ans2=m*g
		ans=d/t
		context= {
			'comments':request.POST.get('comments'),
			'weight':ans2,
            'Gravitational_Force':request.POST.get('Gravitational_Force'),
			'mass':request.POST.get('mass'),
			'time':request.POST.get('time'),
			'distance_travelled':request.POST.get('distance_travelled'),
			'speed':ans
			}

		return render(request,'rpg2.html',context)
                #).save()
				
            #post.author = request.user
            #post.published_date = timezone.now()
           # post.save()
            #return HttpResponseRedirect('https://desolate-falls-15706.herokuapp.com')
    else:
        form = speedandweightForm()
    return render(request, 'rpg.html', {'form': form})	

	
	
	