from django.http.request import host_validation_re
from django.shortcuts import render, reverse, redirect
from django.views.generic.detail import DetailView
from .models import LostItem, FoundItem
from .forms import lostform, foundform
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import DeleteView


def index(request):
    founditem = FoundItem.objects.all()
    lostitem = LostItem.objects.all()
    # item = item = get_object_or_404(LostItem, pk=id)
    context = {'founditem':founditem, 'lostitem':lostitem}
    return render(request, 'lostfound/index.html', context)






def founditemlist(request):
    founditem = FoundItem.objects.all()
    context = {'founditem':founditem}
    return render(request, 'lostfound/founditem_list.html', context)




def founditemdetails(request, id):
    item = get_object_or_404(FoundItem, pk=id)
    return render(request, 'lostfound/found_details.html', {'item':item})


def lostitemdetails(request, id):
    item = get_object_or_404(LostItem, pk=id)
    return render(request, 'lostfound/lost_details.html', {'item':item})



class deletefounditems(DeleteView):
    model = FoundItem    
    template_name = 'lostfound/founditem_delete.html'

    success_url = '/founditem'
    





class deletelostitems(DeleteView):
    model = LostItem
    template_name = 'lostfound/founditem_delete.html'

    success_url = '/'





def createlostitem(request):
    form = lostform()
    if request.method == "POST":
        form = lostform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
            return redirect('/')

    else: 
        print("the form is not saved!")
    return render(request, 'lostfound/form.html', {'form':form})






def createfounditem(request):
    form = foundform()
    if request.method == "POST":
        form = foundform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else: 
        print("the form is now saved!")
    return render(request, 'lostfound/form.html', {'form':form})




def about(request):
    return render(request, 'lostfound/about.html')