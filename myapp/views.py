#views.py
from django.shortcuts import render, redirect
from myapp.models import Member
from myapp.forms import MemberForm

# Create your views here.
def index(request):
    members = Member.objects.all()
    return render(request, 'index.html', { 'members': members })

def add_member(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            Member = form.save()
            return redirect('/')
    else:
        form = MemberForm()
    return render(request, 'add_member.html', { 'form': form })
