from django.shortcuts import get_object_or_404,render
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.shortcuts import redirect 

from .models import Inmueble
from .forms import UploadImageForm, InmuebleForm


# Create your views here.
def index(request):
    latest_publish_list = Inmueble.objects.order_by('-fecha_publicacion')
    template = loader.get_template('smarthome/index.html')
    context = {
        'latest_publish_list': latest_publish_list,
    }
    return HttpResponse(template.render(context, request))

def details(request,pk):
    inmueble = get_object_or_404(Inmueble, pk=pk)
    return render(request, 'smarthome/property-details.html', {'inmueble': inmueble})

def search(request):
    if request.method == "POST":
        response = {}
        for key, value in request.POST.items():
            if str(key) == 'tipo_inmueble' or str(key) == 'tipo_oferta' or str(key) == 'ciudad' or str(key) == 'precio-min' or str(key) == 'precio-max':
                response[str(key)] = str(value) 
    search_list = Inmueble.objects.filter(tipo_inmueble__icontains=response['tipo_inmueble'], 
                    tipo_oferta__icontains=response['tipo_oferta'], 
                    direccion__icontains=response['ciudad'],
                    precio__gte=response['precio-min'], 
                    precio__lte=response['precio-max'])
    context = {
        'search_list': search_list,
    }
    template = loader.get_template('smarthome/index.html')
    return HttpResponse(template.render(context, request))

def upload_image_view(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            message = "Image uploaded succesfully!"
    else:
        form = UploadImageForm()
    context = {
        'publication': form,
    }
    template = loader.get_template('smarthome/upload.html')
    return HttpResponse(template.render(context, request))

def new_publication(request):
    if request.method == "POST":
        form = InmuebleForm(request.POST)
        if form.is_valid():
            inmueble = form.save(commit=False)
            inmueble.fecha_publicacion = timezone.now()
            inmueble.save()
            return redirect('details', pk=inmueble.pk)
    else:
        form = InmuebleForm()
    return render(request, 'smarthome/publication_edit.html', {'form': form})

