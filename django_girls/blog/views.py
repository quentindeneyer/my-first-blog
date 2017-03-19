# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Workshop, Organizer
from .forms import WorkshopForm #, OrganizerForm


def workshop_list(request):
    workshops = Workshop.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    if request.user.is_authenticated():
        workshops = Workshop.objects.filter(organizer__administrator=request.user)
    return render(request, 'blog/workshop_list.html', {'workshops': workshops,'request': request})

def workshop_detail(request,pk):
	workshop = get_object_or_404(Workshop, pk=pk)
	return render(request, 'blog/workshop_detail.html',{'workshop': workshop})

def workshop_new(request):
    if request.method == "POST" and Organizer.objects.get(pk=request.POST.get('organizer')) in request.user.organizer_set.all():
        if 'delete' in request.POST:
                return redirect('workshop_list')
        else:
            form = WorkshopForm(request.POST)
            if form.is_valid():
                workshop = form.save(commit=False)
                workshop.author = request.user
                workshop.created_date = timezone.now()
                workshop.save()
                return redirect('workshop_list')
    else:
        default_data = {'organizer': request.user.organizer_set.all()[0], 'url_information': 'http://','contact_email': request.user.organizer_set.all()[0].contact_email}
        # form = WorkshopForm(default_data)
        form = WorkshopForm(initial=default_data)
    return render(request, 'blog/workshop_edit.html', {'form': form})

def workshop_edit(request, pk):
    workshop = get_object_or_404(Workshop, pk=pk)
    if workshop.organizer in request.user.organizer_set.all():
        if request.method == "POST":
            if 'delete' in request.POST:
                workshop.delete()
                return redirect('workshop_list')
            else:
                form = WorkshopForm(request.POST, instance=workshop)
                if form.is_valid():
                    workshop = form.save(commit=False)
                    workshop.author = request.user
                    workshop.created_date = timezone.now()
                    workshop.save()
                    return redirect('workshop_list')

        else:
            form = WorkshopForm(instance=workshop)
        return render(request, 'blog/workshop_edit.html', {'form': form})
    else:
        return redirect('workshop_list')


#---------------------------------------------------------------------------------
def organizer_list(request):
    organizers = Organizer.objects.all()
    return render(request, 'blog/organizer_list.html', {'organizers': organizers})

def get_user_profile(request):
    return User.username

# def organizer_detail(request,pk):
#     organizer = get_object_or_404(Organizer, pk=pk)
#     return render(request, 'blog/organizer_detail.html',{'organizer': organizer})

# def organizer_new(request):
#     if request.method == "POST":
#         form = OrganizerForm(request.POST)
#         if form.is_valid():
#             organizer = form.save(commit=False)
#             organizer.author = request.user
#             organizer.created_date = timezone.now()
#             organizer.save()
#             return redirect('organizer_detail', pk=organizer.pk)
#     else:
#         form = OrganizerForm()
#     return render(request, 'blog/organizer_edit.html', {'form': form})

# def organizer_edit(request, pk):
#     organizer = get_object_or_404(Organizer, pk=pk)
#     if request.method == "POST":
#         form = OrganizerForm(request.POST, instance=organizer)
#         if form.is_valid():
#             organizer = form.save(commit=False)
#             organizer.author = request.user
#             organizer.created_date = timezone.now()
#             organizer.save()
#             return redirect('organizer_detail', pk=organizer.pk)
#     else:
#         form = OrganizerForm(instance=organizer)
#     return render(request, 'blog/organizer_edit.html', {'form': form})