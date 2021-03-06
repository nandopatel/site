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

def stunningsingapore(request):
	return render(request,'stunningsingapore.html')

def gallery(request):
	return render(request,'Gallery.html')
def rpg(request):
	
	inventory = {
		'exp':1,
	   'logs':0
	}
	return render(request,'rpg.html',inventory)
def formulas(request):
	form = form(request.POST)
	
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

	cal=re.sub(r'(>)(.*?</text>)',r'fill=grey\1\2',str(lst[0]))
	
	svg_def='<svg class="js-calendar-graph-svg" height="104" width="676">'
	svg_def_new='<svg class="js-calendar-graph-svg" height="104" width="676" align="center">'
	cal=re.sub(svg_def,svg_def_new,cal)
	cal='<div text-align="center">'+cal+'</div>'
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
	
 
 	pivx_data = requests.get("https://coinmarketcap.com/currencies/pivx/")
	f = re.findall('quote_price.*',pivx_data.content)
	fclean = f[0].replace('quote_price">','').replace('</span>','').replace('<span class="text-large  positive_change ">','').replace('<span class="text-large  negative_change">','')
	pivx_price,pivx_percent_change=fclean.split(' ')
	
	
	btc_data = requests.get("https://coinmarketcap.com/currencies/bitcoin/")
	f2 = re.findall('quote_price.*',btc_data.content)
	fclean2 = f2[0].replace('quote_price">','').replace('</span>','').replace('<span class="text-large  positive_change ">','').replace('<span class="text-large  negative_change">','')
	btc_price,btc_percent_change=fclean2.split(' ')


	rise_data = requests.get("https://coinmarketcap.com/currencies/rise/")
	f3 = re.findall('quote_price.*',rise_data.content)
	fclean3 = f3[0].replace('quote_price">','').replace('</span>','').replace('<span class="text-large  positive_change ">','').replace('<span class="text-large  negative_change">','')
	rise_price,rise_percent_change=fclean3.split(' ')

	ark_data = requests.get("https://coinmarketcap.com/currencies/ark/")
	f4 = re.findall('quote_price.*',ark_data.content)
	fclean4 = f4[0].replace('quote_price">','').replace('</span>','').replace('<span class="text-large  positive_change ">','').replace('<span class="text-large  negative_change">','')
	ark_price,ark_percent_change=fclean4.split(' ')
	
	dash_data = requests.get("https://coinmarketcap.com/currencies/dash/")
	f5 = re.findall('quote_price.*',dash_data.content)
	fclean5 = f5[0].replace('quote_price">','').replace('</span>','').replace('<span class="text-large  positive_change ">','').replace('<span class="text-large  negative_change">','')
	dash_price,dash_percent_change=fclean5.split(' ')

	ethereum_data = requests.get("https://coinmarketcap.com/currencies/ethereum/")
	f6 = re.findall('quote_price.*',ethereum_data.content)
	fclean6 = f6[0].replace('quote_price">','').replace('</span>','').replace('<span class="text-large  positive_change ">','').replace('<span class="text-large  negative_change">','')
	ethereum_price,ethereum_percent_change=fclean6.split(' ')

	iop_data = requests.get("https://coinmarketcap.com/currencies/internet-of-people/")
	f7 = re.findall('quote_price.*',iop_data.content)
	fclean7 = f7[0].replace('quote_price">','').replace('</span>','').replace('<span class="text-large  positive_change ">','').replace('<span class="text-large  negative_change">','')
	iop_price,iop_percent_change=fclean7.split(' ')

	context = {"pivx_price":pivx_price,"pivx_percent_change":pivx_percent_change,"btc_price":btc_price,"btc_percent_change":btc_percent_change,"rise_price":rise_price,"rise_percent_change":rise_percent_change,"ark_price":ark_price,"ark_percent_change":ark_percent_change,"dash_price":dash_price,"dash_percent_change":dash_percent_change,"ethereum_price":ethereum_price,"ethereum_percent_change":ethereum_percent_change,"iop_price":iop_price,"iop_percent_change":iop_percent_change} 
	return render(request,'rpg.html',context)	

