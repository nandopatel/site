from django.shortcuts import render
#from .forms import NameForm
from django.http import HttpResponseRedirect
from django.http import HttpResponse
import os
from time import sleep
from random import randint
#from tqdm import tqdm
import sys 

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
	context={'X':55}
	return render(request,'portfolio.html',context)
	
	
	
from .forms import speedandweightForm

def feedback(request):
    if request.method == "POST":
		#form = speedandweightForm(request.POST)
		
		context= {
			'comments':request.POST.get('comments'),
			'weight':request.POST.get('weight'),
            'Gravitational_Force':request.POST.get('Gravitational_Force'),
			'mass':request.POST.get('mass'),
			'time':request.POST.get('time'),
			'distance_travelled':request.POST.get('distance_travelled'),
			'speed':request.POST.get('distance_travelled')/request.POST.get('time'),
			}

		return render(request,'rpg.html',context)
                #).save()
				
            #post.author = request.user
            #post.published_date = timezone.now()
           # post.save()
            #return HttpResponseRedirect('https://desolate-falls-15706.herokuapp.com')
    else:
        form = speedandweightForm()
    return render(request, 'rpg.html', {'form': form})	

	
	
	