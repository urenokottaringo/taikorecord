from django.shortcuts import render

# Create your views here.
from django.views import generic
from taikorecord.models import Music, Genre, Log
from django.shortcuts import redirect, get_object_or_404
from .form import GenreForm, MusicForm, LogForm

class IndexView(generic.ListView):
    template_name = 'taikorecord/index.html'
    context_object_name = 'music_list'
    
    queryset= Music.objects.all().order_by("diff")
    #.order_by("result_date").order_by("genre").order_by("title")
    

def musicdetail(request, pk):
    m = Music.objects.get(pk=pk)
    return render(request, 'taikorecord/detail.html', {'music': m})
    
def registergenre(request):
    if request.method == "POST":
        form = GenreForm(request.POST)
        if form.is_valid():
            d = form.save(commit=False)
            d.save()
            return redirect('taikorecord:registermusic')
    else:
        form = GenreForm()
        return render(request, 'taikorecord/register.html', {'form': form})
    
def registermusic(request):
    if request.method  == "POST":
        form = MusicForm(request.POST)
        if form.is_valid():
            m = form.save(commit=False)
            m.save()
            return redirect('taikorecord:music_detail', pk=m.pk)
    else:
        form = MusicForm()
        return render(request, 'taikorecord/register.html', {'form': form})

def writinglog(request):
    if request.method == "POST":
        form = LogForm(request.POST)
        if form.is_valid():
            l = form.save(commit=False)
            l.save()
            return redirect('taikorecord:music_detail', pk=l.music.pk)
    else:
        form = LogForm()
        return render(request, 'taikorecord/register.html', {'form': form})
    
def updatelog(request, pk):
    obj = get_object_or_404(Log, id=pk)
    if request.method == "POST":
        form = LogForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('taikorecord:music_detail', pk=obj.music.pk)
    else:
        form = LogForm(instance=obj)
        return render(request, 'taikorecord/register.html', {'form': form}) 

def deletelog(request, pk):
    obj = get_object_or_404(Log, id=pk)
    music_id = obj.music.pk
    if request.method =="POST": 
        obj.delete() 
        return redirect('taikorecord:music_detail', pk=music_id)
    context = {'obj':obj}
    return render(request, "taikorecord/delete.html", context)

def deletemusic(request, pk):
    obj = get_object_or_404(Music, id=pk)
    if request.method == "POST":
        obj.delete()
        return redirect('taikorecord:index')
    context = {'obj':obj}
    return render(request, "taikorecord/delete.html", context)

def writingthismusiclog(request, pk):
    obj = get_object_or_404(Music, id=pk)
    form = LogForm({'music':obj})
    if request.method == "POST":
        form = LogForm(request.POST)
        if form.is_valid():
            l = form.save(commit=False)
            l.save()
            return redirect('taikorecord:music_detail', pk=l.music.pk)
    else:
        return render(request, "taikorecord/register.html", {'form': form})