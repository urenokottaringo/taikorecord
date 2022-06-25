from django.shortcuts import render

# Create your views here.
from django.views import generic
from myapp.models import Movie, Director, Log
from django.shortcuts import redirect, get_object_or_404
from .form import DirectorForm, MovieForm, LogForm

def index(request):
    movie_list = Movie.objects.all()
    return render(request, 'myapp/index.html', {'movie_list': movie_list})


def moviedetail(request, pk):
    m = Movie.objects.get(pk=pk)
    return render(request, 'myapp/detail.html', {'movie': m})
    
def registerdirector(request):
    if request.method == "POST":
        form = DirectorForm(request.POST)
        if form.is_valid():
            d = form.save(commit=False)
            d.save()
            return redirect('myapp:registermovie')
    else:
        form = DirectorForm()
        return render(request, 'myapp/register.html', {'form': form})
    
def registermovie(request):
    if request.method  == "POST":
        form = MovieForm(request.POST)
        if form.is_valid():
            m = form.save(commit=False)
            m.save()
            return redirect('myapp:movie_detail', pk=m.pk)
    else:
        form = MovieForm()
        return render(request, 'myapp/register.html', {'form': form})

def writinglog(request):
    if request.method == "POST":
        form = LogForm(request.POST)
        if form.is_valid():
            l = form.save(commit=False)
            l.save()
            return redirect('myapp:movie_detail', pk=l.movie.pk)
    else:
        form = LogForm()
        return render(request, 'myapp/register.html', {'form': form})
    
def updatelog(request, pk):
    obj = get_object_or_404(Log, id=pk)
    if request.method == "POST":
        form = LogForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('myapp:movie_detail', pk=obj.movie.pk)
    else:
        form = LogForm(instance=obj)
        return render(request, 'myapp/register.html', {'form': form}) 

def deletelog(request, pk):
    obj = get_object_or_404(Log, id=pk)
    movie_id = obj.movie.pk
    if request.method =="POST": 
        obj.delete() 
        return redirect('myapp:movie_detail', pk=movie_id)
    context = {'obj':obj}
    return render(request, "myapp/delete.html", context)

def deletemovie(request, pk):
    obj = get_object_or_404(Movie, id=pk)
    if request.method == "POST":
        obj.delete()
        return redirect('myapp:index')
    context = {'obj':obj}
    return render(request, "myapp/delete.html", context)

def writingthismovielog(request, pk):
    obj = get_object_or_404(Movie, id=pk)
    form = LogForm({'movie':obj})
    if request.method == "POST":
        form = LogForm(request.POST)
        if form.is_valid():
            l = form.save(commit=False)
            l.save()
            return redirect('myapp:movie_detail', pk=l.movie.pk)
    else:
        return render(request, "myapp/register.html", {'form': form})