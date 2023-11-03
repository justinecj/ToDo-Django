from django.shortcuts import render, redirect


from . models import *
from . forms import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
class TaskListview(ListView):
    model = Entity
    template_name = 'home.html'
    context_object_name = 'datas'
class TaskDetailview(DetailView):
    model = Entity
    template_name = 'detailview.html'
    context_object_name = 'task'
class TaskUpdateview(UpdateView):
    model = Entity
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('name','priority','date')

    def get_success_url(self):
        return reverse_lazy('gvdetail',kwargs={'pk':self.object.id})
class TaskDeleteview(DeleteView):
    model = Entity
    template_name = 'delete.html'
    success_url = reverse_lazy('gvhome')




def home(request):
    if request.method == 'POST':
        entity = request.POST.get('entity','')
        priority = request.POST.get('priority','')
        date = request.POST.get('date', '')
        data = Entity(name=entity, priority=priority, date=date)
        data.save()
    datas = Entity.objects.all()
    return render(request, 'home.html',{'datas':datas})
def delete(request, id):
    if request.method == 'POST':
        data = Entity.objects.get(id=id)
        data.delete()
        return redirect('/')
    return render(request, 'delete.html')
def update(request, id):
    data = Entity.objects.get(id=id)
    form = ToDoForm(request.POST or None, request.FILES, instance=data)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'update.html', {'data':data,'form':form})