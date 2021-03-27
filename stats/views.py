from django.shortcuts import render, get_object_or_404, redirect
from .forms import DescriptiveStatsForm
from .models import DescriptiveStats

def descriptivestats_create_view(request):
    form = DescriptiveStatsForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = DescriptiveStatsForm()
    context = {
        'form': form
    }
    return render(request, "descriptivestats/descriptivestats_create.html", context)


def descriptivestats_update_view(request, id=id):
    obj = get_object_or_404(DescriptiveStats, id=id)
    form = DescriptiveStatsForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "descriptivestats/descriptivestats_create.html", context)


def descriptivestats_list_view(request):
    queryset = DescriptiveStats.objects.all() # list of objects
    context = {
        "object_list": queryset
    }
    return render(request, "descriptivestats/descriptivestats_list.html", context)

def descriptivestats_detail_view(request, id):
    obj = get_object_or_404(DescriptiveStats, id=id)
    context = {
        "object": obj
    }
    return render(request, "descriptivestats/descriptivestats_detail.html", context)


def descriptivestats_delete_view(request, id):
    obj = get_object_or_404(DescriptiveStats, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('../../')
    context = {
        "object": obj
    }
    return render(request, "descriptivestats/descriptivestats_delete.html", context)
    