from django.shortcuts import ( 
    render,
    redirect,
    get_object_or_404, 
)
from django.http import HttpResponse
from .models import Message
from .forms import TimeForm

def index(request):
      return render(request, 'wsp_time/index.html', {})


def add(request):
    return render(request, 'wsp_time/edit.html', {})


def edit(request, editing_id):
    return render(request, 'wsp_time/edit.html', {})


def delete(request):
    return HttpResponse('Delete')

def index(request):
    d = {
        'messages': Message.objects.all(),
    }
    return render(request, 'wsp_time/index.html', d)

def add(request):
    form = TimeForm(request.POST or None)
    if form.is_valid():
       Time.objects.create(**form.cleaned_data)
       return redirect('wsp_time:index')

    d = {
       'form': form,
    }
    return render(request, 'wsp_time/edit.html', d)

def edit(request, editing_id):
    message = get_object_or_404(Message, id=editing_id)
    if request.method == 'POST':
        form = TimeForm(request.POST)
        if form.is_valid():
            message.message = form.cleaned_data['message']
            message.save()
            return redirect('wsp_time:index')
    else:
      # GETリクエスト（初期表示）時はDBに保存されているデータをFormに結びつける
       form = TimeForm({'message': message.message})
    d = {
        'form': form,
    }

    return render(request, 'wsp_time/edit.html', d)


#from django.http import Http404
#try:
#    message = Message.objects.get(id=editing_id)
#except Message.DoesNotExist:
#      raise Http404
