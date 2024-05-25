from django.shortcuts import render, redirect
from .forms import MediaFileForm
from .models import MediaFile


def base(request):
    database_content = ProfileImages.objects.all()
    context = {'database_content': database_content}
    return render(request, 'base.html', context )


def index(request):
    return render(request, 'bincom5.html')


def gallery(request):
    multimedia_data = MediaFile.objects.all()
    context = {'database': multimedia_data}
    return render(request, 'gallery.html', context)


def upload_file(request):
    if request.method == 'POST':
        form = MediaFileForm(request.POST, request.FILES)
#        form2 = ProfileImagesForm(request.POST, request.FILES)
        if form.is_valid(): # and form2.is_valid():
            form.save()
            #form2.save()
            return redirect('gallery')
    else:
        form = MediaFileForm()
    return render(request, 'upload.html', {'form': form})
