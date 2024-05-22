from django.shortcuts import render, redirect
from .forms import MediaFileForm
from django.http import HttpResponse
from django.template import loader
from .models import MediaFile

# Create your views here.
def index(request):
	template = loader.get_template('bincom5.html')
	return HttpResponse(template.render())


def gallery(request):
     multimedia_data = MediaFile.objects.all().values()
     context = {'database': multimedia_data}
     return render(request, 'gallery.html', context)

     


def upload_file(request):
    if request.method == 'POST':
        form = MediaFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = MediaFileForm()
            success_message = {'success': 'success', 'form': form,}
            return render(request, 'upload.html', {'success': success_message} )
            

            
    else:
        form = MediaFileForm()
    return render(request, 'upload.html', {'form': form})



