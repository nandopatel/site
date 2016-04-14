from django.shortcuts import render

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
		
	
	}
		

		

	return render(request,'rpg.html',context)