# Create your views here.
from django.core.context_processors import csrf
from django.shortcuts import render_to_response, HttpResponse
from calend.models import StoredData
import re;
def calendar_form(request):
    return render_to_response('calendar.html')

def send(request):
    errors = []
    c = {}
    c.update(csrf(request))
    if request.method == 'POST':
	if not request.POST.get('name', ''):
            errors.append('Enter a name.')
	elif len(request.POST['name']) > 6:
            errors.append('Name must be less or equal 6 symbols.')
	
        if not request.POST.get('date', ''):
            errors.append('Enter a date.')
	elif not re.match('^[0-9]{4}-[0-9]{2}-[0-9]{2}$', request.POST['date']) is not None:
	    errors.append('Date must be in ATOM format (YYYY-mm-dd).')

	if not errors:
		sd = StoredData(name = request.POST['name'], date = request.POST['date'])
		sd.save()
    		return render_to_response('count.html', {'counter': StoredData.objects.count()})
    return render_to_response('calendar.html', dict({'errors': errors}.items() + c.items()))
