from django.shortcuts import render

def recordatorio_view(request):
	return render(request, 'recordatorio.html')
