from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request,'index.html')

def booking(request):
	return render(request,'booking.html')
	
def currency(request):
	return render(request,'currency.html')

def gallery(request):
	return render(request,'gallery.html')