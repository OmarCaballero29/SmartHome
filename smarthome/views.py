from django.shortcuts import get_object_or_404,render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.shortcuts import redirect
from django.forms import modelformset_factory, inlineformset_factory
from django.contrib import messages

from .models import Inmueble, Images
from .forms import InmuebleForm, ImageForm


# Create your views here.
def index(request):
    latest_publish_list = Inmueble.objects.order_by('-fecha_publicacion')
    images = Images.objects.all().distinct().order_by('-inmueble_id')
    template = loader.get_template('smarthome/index.html')
    context = {
        'latest_publish_list': latest_publish_list,
        'images': images,
    }
    return HttpResponse(template.render(context, request))

def details(request,pk):
    inmueble = get_object_or_404(Inmueble, pk=pk)
    images = inmueble.images_set.all()
    return render(request, 'smarthome/property-details.html', {'inmueble': inmueble,'images':images})

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
                    precio__lte=response['precio-max']).distinct().order_by('-fecha_publicacion')
    images = Images.objects.all().distinct().order_by('-inmueble_id')

    context = {
        'search_list': search_list,
        'images': images,
    }
    template = loader.get_template('smarthome/index.html')
    return HttpResponse(template.render(context, request))

@login_required
def new_publication(request):
    ImageFormSet = modelformset_factory(Images,
                                        form=ImageForm, max_num=12, extra=12, exclude=('inmueble',))
    if request.method == "POST":
        form = InmuebleForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES,
                               queryset=Images.objects.none())
        if form.is_valid() and formset.is_valid():
            inmueble = form.save(commit=False)
            inmueble.fecha_publicacion = timezone.now()
            inmueble.disponible = True
            inmueble.save()

            for form in formset.cleaned_data:
                #this helps to not crash if the user   
                #do not upload all the photos
                if form:
                    image = form['image']
                    photo = Images(inmueble=inmueble, image=image)
                    photo.save()
            return redirect('details', pk=inmueble.pk)
        else:
            print(form.errors, formset.errors)
    else:
        form = InmuebleForm()
        formset = ImageFormSet(queryset=Images.objects.none())
    return render(request, 'smarthome/publication_edit.html', {'form': form, 'formset': formset})

@login_required
def publication_edit(request, pk):
    inmueble = get_object_or_404(Inmueble, pk=pk)
    ImageInLineFormSet = inlineformset_factory(Inmueble, Images, max_num=12, exclude=('inmueble',))

    if request.method == "POST":
        form = InmuebleForm(request.POST, instance=inmueble)
        formset = ImageInLineFormSet(request.POST, request.FILES, instance=inmueble)
        
        if form.is_valid() and formset.is_valid():
            inmueble = form.save()
            formset.save()

            return redirect('details', pk=inmueble.pk)
        else:
            print(form.errors, formset.errors)
    else:
        form = InmuebleForm(instance=inmueble)
        formset = ImageInLineFormSet(instance=inmueble)
    return render(request, 'smarthome/publication_edit.html', {'form': form, 'formset': formset })