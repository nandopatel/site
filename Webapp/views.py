from django.shortcuts import render

# Create your views here.
def base(request):
	return render(request,'base.html')

def booking(request):
	return render(request,'booking.html')
	
def currency(request):
	return render(request,'currency.html')

def gallery(request):
	return render(request,'gallery.html')