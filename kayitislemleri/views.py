from django.shortcuts import render, get_object_or_404
from .models import Personel
from .forms import PostForm
from django.shortcuts import redirect
from django.utils  import  timezone


def personel_list(request):
    personeller=Personel.objects.all()
    return render(request, 'kayitislemleri/personel_kayit.html', {'personeller':personeller})

def personel_detail(request, pk):
    personel = get_object_or_404(Personel, pk=pk)
    return render(request, 'kayitislemleri/personel_detail.html', {'personel': personel})

def personel_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            personel = form.save(commit=False)
            personel.created_date = timezone.now()
            personel.save()
            return redirect('personel_detail', pk=personel.pk)
    else:
        form = PostForm()
    return render(request, 'kayitislemleri/personel_add.html', {'form': form})

def delete_personel(request,pk):
    template = 'kayitislemleri/personel_kayit.html'
    personel = get_object_or_404(Personel, pk=pk)
    personel.delete()
    return  render(request,template,{'personeller':Personel.objects.all()})

def personel_edit(request,pk):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            personel = form.save(commit=False)
            personel.pk=pk
            personel.created_date = timezone.now()
            personel.save()
            return redirect('personel_detail', pk=personel.pk)
    else:
        form = PostForm()
    return render(request, 'kayitislemleri/personel_edit.html', {'form': form})