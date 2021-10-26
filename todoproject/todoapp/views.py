from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import task
from .form import todoform
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView

class tasklistview(ListView):
    model=task
    template_name='home.html'
    context_object_name='task'

class taskdetialview(DetailView):
    model = task
    template_name = 'detail.html'
    context_object_name = 'task'

class taskupdateview(UpdateView):
    model = task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('name','priority','date')

    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})

class taskdeleteview(DeleteView):
    model = task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvhome')



# Create your views here.
def add(request):
    test1 = task.objects.all()
    if request.method=='POST':
        name=request.POST.get('task','')
        priority= request.POST.get('priority','')
        date=request.POST.get('date','')
        test=task(name=name,priority=priority,date=date)

        test.save()
    return render(request,'home.html',{'task': test1})
# def details(request):
#   test1 = task.objects.all()
#  return render(request, 'detail.html', {'task': test1})
def delete(request,taskid):
    task1=task.objects.get(id=taskid)
    if request.method=='POST':
        task1.delete()
        return redirect('/')

    return render(request,'delete.html')
def update(request,id):
    task2=task.objects.get(id=id)
    form=todoform(request.POST or None, instance=task2)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'task':task2})
