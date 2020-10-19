from django.shortcuts import render
import datetime
# Create your views here.

def Welcome_clint(request):
	date=datetime.datetime.now()
	hour=int(datetime.datetime.now().hour)
	msg='Hi Asshole'

	if hour<=12:
		msg=msg+ 'Morning'

	elif hour<=16:
		msg=msg+ 'Afternoon'

	elif hour<=21:
		msg=msg+ 'Evening'

	else:
		msg=msg+'Night'

	my_dict={'insert_date' :date, 'insert_msg' :msg}
	return render(request=request,template_name='app9/display.html',context=my_dict)