from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic
from django.forms import modelformset_factory
from .e_form import EditData,EditDispatch
from .forms import (

    OrderPoAndPurchaserModelForm,
    OrderDetailsFormset
)
from .models import OrderPoAndPurchaser, OrderDetails
# Create your views here.


def index(request):
    return render(request,'index.html')


def order(request):
    template_name = 'order.html'
    if request.method == 'GET':
        bookform = OrderPoAndPurchaserModelForm(request.GET or None)
        formset = OrderDetailsFormset(queryset=OrderDetails.objects.none())
    elif request.method == 'POST':
        bookform = OrderPoAndPurchaserModelForm(request.POST)
        formset = OrderDetailsFormset(request.POST)
        if bookform.is_valid() and formset.is_valid():
            # first save this PoAndPurchaser, as its reference will be used in `Details`
            poAndPurchaser = bookform.save()
            for form in formset:
                # so that `poAndPurchaser` instance can be attached.
                details = form.save(commit=False)
                details.OrderPoAndPurchaser = poAndPurchaser
                details.save()
            return redirect('show')
    return render(request, template_name, {
        'bookform': bookform,
        'formset': formset,
    })


def show(request):
    Order_PoAndPurchaser = OrderPoAndPurchaser.objects.all()
    Order_Details = OrderDetails.objects.all()
    i=1



    return render(request, 'show.html', {'Order_PoAndPurchaser': Order_PoAndPurchaser, 'i':i})


def dispatcher(request):
    Order_PoAndPurchaser = OrderPoAndPurchaser.objects.all()



    return render(request, 'dispatcher.html', {'Order_PoAndPurchaser': Order_PoAndPurchaser})

def editDispatch(request,id=None):

   p = OrderDetails.objects.get(pk=id)

   form = EditDispatch(request.POST or None,instance=p)
   print("not save")

   if form.is_valid():
       form.save()
       print('saved')
       return redirect('dispatcher')
   print("not save!")

   return render(request,'edit_dispatch.html',{'form':form})


def edit(request,id=None):

    p = OrderDetails.objects.get(pk=id)

    form=EditData(request.POST or None,instance=p)

    if form.is_valid():
        form.save()
        return redirect('show')

    return render(request,'edit.html',{'form':form})







def delete(request,id=None):

    if request.method=='POST':
        p=OrderDetails.objects.get(pk=id)
        p.delete()
        return redirect('show')

    return render(request,'delete.html')