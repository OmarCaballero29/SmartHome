from django.shortcuts import get_object_or_404,render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.shortcuts import redirect
from django.forms import modelformset_factory, inlineformset_factory
from django.contrib import messages
from django.contrib.auth.models import User


from .models import Inmueble, Images
from .forms import InmuebleForm, ImageForm, UserRegisterForm


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
            if str(key) == 'tipo_inmueble' or str(key) == 'tipo_oferta' or str(key) == 'ciudad' or str(key) == 'precio_min' or str(key) == 'precio_max':
                response[str(key)] = str(value) 
    search_list = Inmueble.objects.filter(tipo_inmueble__icontains=response['tipo_inmueble'], 
                    tipo_oferta__icontains=response['tipo_oferta'], 
                    direccion__icontains=response['ciudad'],
                    precio__gte=response['precio_min'], 
                    precio__lte=response['precio_max']).distinct().order_by('-fecha_publicacion')
    images = Images.objects.all().distinct().order_by('-inmueble_id')
    context = {
        'search_list': search_list,
        'images': images,
        'response': response,
    }
    template = loader.get_template('smarthome/index.html')
    return HttpResponse(template.render(context, request))

@login_required
def new_publication(request):
    ERR = ""
    ImageFormSet = modelformset_factory(Images,
                                        form=ImageForm, max_num=12, extra=12, exclude=('inmueble',))
    if request.method == "POST":
        form = InmuebleForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES,
                               queryset=Images.objects.none())

        direct = request.POST["direccion"]
        duplicados = Inmueble.objects.filter(direccion__icontains = direct)
        if form.is_valid() and formset.is_valid() and duplicados.count() < 1:
            inmueble = form.save(commit=False)
            inmueble.propietario = request.user
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
            if(duplicados.count() >= 1): ERR = "La vivienda que desea ingresar ya existe"
    else:
        form = InmuebleForm()
        formset = ImageFormSet(queryset=Images.objects.none())
    return render(request, 'smarthome/publication_edit.html', {'form': form, 'formset': formset, 'Perror': ERR})

@login_required
def publication_edit(request, pk):
    inmueble = get_object_or_404(Inmueble, pk=pk)
    ImageInLineFormSet = inlineformset_factory(Inmueble, Images, max_num=12, exclude=('inmueble',))
    ERR = ""

    if request.method == "POST":
        form = InmuebleForm(request.POST, instance=inmueble)
        formset = ImageInLineFormSet(request.POST, request.FILES, instance=inmueble)
        
        #checa inmuebles con esa direccion
        direct = request.POST["direccion"]
        duplicados = Inmueble.objects.filter(direccion__icontains = direct)

        user = request.user.username
        prop = duplicados[0].propietario.username

        #verifica las coincidencias
        if (duplicados.count() < 1): coincidencia_valida = True
        
        #si hay coincidencias entonces checa que solo sea la del inmueble a editar
        if(duplicados.count() == 1): 
            coincidencia_valida = (user == prop) 

        if form.is_valid() and formset.is_valid() and  coincidencia_valida:
            inmueble = form.save()
            formset.save()
            return redirect('details', pk=inmueble.pk)
        else:
            print(form.errors, formset.errors)
            if(duplicados.count() >= 1): ERR = "La vivienda que desea ingresar ya existe"
    else:
        form = InmuebleForm(instance=inmueble)
        formset = ImageInLineFormSet(instance=inmueble)

    return render(request, 'smarthome/publication_edit.html', {'form': form, 'formset': formset, 'Perror': ERR})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado con exito')
            return redirect('login')
    else:
        form = UserRegisterForm()

    context = {'form': form}
    return render(request, 'smarthome/register.html', context)

@login_required
def favorite(request, fav_id):
    inmueble = get_object_or_404(Inmueble, id=fav_id)
    inmueble.favorito.add(request.user)         
    return redirect('favorites')

@login_required
def list_favorites(request):
    inmuebles_fav = Inmueble.objects.filter(favorito=request.user)
    images = Images.objects.all().distinct()
    return render(request, 'smarthome/favorites.html',{'inmuebles_fav':inmuebles_fav, 'images':images})

def contact(request):
    return render(request,'smarthome/contact.html')