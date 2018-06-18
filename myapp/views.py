from django.shortcuts import render
from .forms import data
# Create your views here.

def index(request):
    form = data(request.POST or None)
    x = 0
    on=False
    if form.is_valid():
        a = form.cleaned_data['a']
        b = form.cleaned_data['b']
        if a>b:
            x=a
        else:
            x=b
        on=True
    context = {'form': form, 'x': x,'on':on}
    return render(request, 'index.html', context)
