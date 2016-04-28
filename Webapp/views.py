from django.shortcuts import render
from django.http import HttpResponse
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
def formulas(request):
	return render(request,'formulas.html')

	import os
	from time import sleep
	from random import randint
	#from tqdm import tqdm
	import sys 


	def start():
		#startchoice = raw_input("Would you like to start the game ('y' for yes)?: ")
		global startcomment,getlogs,goblincomment,givelogs
		
		startchoice = 'y'
		if startchoice == "y":
			startcomment = """You start off in the world, level yourself up, 
			gain resources and smash enemies. 
			Start by chopping some wood to level your woodchopping"""
			getlogs=chopwood()
			#goblincomment,givelogs=randomeventgoblin()
			getexp()
			seeinventory()
		else:
			print "Shutting down..."
			exit
			
			
		return startcomment,getlogs
		


	def chopwood(inventory=inventory):
		sys.stdout.flush()
		
		#for x in tqdm(range(1,200000)):
			#pass
		getlogs = "+5 logs"
		inventory['logs'] += 5
		return getlogs

	def seeinventory():
		print inventory

	def randomeventgoblin(inventory=inventory):    
		randomnumber = randint(0, 10)
		levelnumber = randint(5, 10)
		if randomnumber >= 5:
			goblincomment = "You stumble across a level {} goblin, he is too high level to battle you so he wants some logs.".format(levelnumber)
			givelogs = "You give him 2 logs"
			inventory['logs'] -= 2
			#print inventory
			return goblincomment, givelogs
			
	def test_form(request):
		return render(request,'test_form.html')
			
	def getexp(inventory=inventory):
		multiplyer = inventory['exp']/10
		#print multiplyer
		#print multiplyer/100.0
		#print int(3+multiplyer/100.0)
		inventory['exp']=inventory['logs']*(3+multiplyer/100.0)
		inventory['exp'] = int(inventory['exp'])
	start()	
	context={
		"startcomment":startcomment,
		"getlogs":getlogs,
		
		"inventory":inventory,
		'exp':inventory['exp'],
		
	
	}
		

		

	return render(request,'rpg.html',context)
	
from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import NameForm

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            #return HttpResponse('<html><p>hello</p>'+str(form.data['your_name'])+' '+str(form.data['your_move'])+'</html>')
			return render(request, 'rpg.html', {
			'name': form.data['your_name'],
			'move': form.data['your_move'],
			'YesNo': form.data['yesorno'],
			
			})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

		
		
    return render(request, 'rpg.html', {'form': form})
	
	
	
	
	
	
def textgen(request):
	import string
	import random
	import time

	possibleCharacters = string.ascii_lowercase + string.digits + string.ascii_uppercase + ' .,!?;:'
	target = "Welcome"
	attemptThis = ''.join(random.choice(possibleCharacters) for i in range(len(target)))
	attemptNext = ''

	completed = False

	generation = 0
	lst=[]
	while completed == False:
		lst.append(attemptThis)
		attemptNext = ''
		completed = True
		for i in range(len(target)):
			if attemptThis[i] != target[i]:
				completed = False
				attemptNext += random.choice(possibleCharacters)
			else:
				attemptNext += target[i]
		generation += 1
		attemptThis = attemptNext
		

	lst.append("Target matched! That took " + str(generation) + " generation(s)")	
	context={'list':lst}
	return render(request,'rpg.html',context)

	
	
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
	
	
	
	
	