import datetime
from django.shortcuts import redirect, render
from user.models import Authen_User
from .form import AnnouncementForm
from .models import AnnouncementModel, typeOfAnnouncement
from django.contrib.auth.decorators import permission_required

@permission_required('announcement.view_announcement')
def viewAnnounce(request):
    announcements = AnnouncementModel.objects.filter(is_active=True)
    typeDict = {t[0]: t[1] for t in typeOfAnnouncement}
    for announcement in announcements:
        announcement.type = typeDict[announcement.type]
    print(announcements)
    context = {
        'announcements': announcements
    }

    return render(request, 'announcement/view_announcement.html', context=context)

@permission_required('announcement.add_announcement')
def announce(request):
    admin = request.user.authen_user.getAdmin()

    if request.method == 'POST':
        form = AnnouncementForm(request.POST)
        if form.is_valid():
            object_announce = form.save()
            object_announce.adminId = admin
            object_announce.save()
            print('Create Announcement --', admin.user.username)
            return redirect('view_announcement')
    else:
        form = AnnouncementForm()
    
    context = {
        'form': form,
        'title': 'Add Anouncement'
    }

    return render(request, 'announcement/add_announcement.html', context=context)

@permission_required('announcement.change_announcement')
def editAnnounce(request, announcement_id):
    admin = request.user.authen_user.getAdmin()
    announcement = AnnouncementModel.objects.get(pk=announcement_id)

    if request.method == 'POST':
        form = AnnouncementForm(request.POST, instance=announcement)
        if form.is_valid():
            object_announce = form.save()
            object_announce.adminId = admin
            object_announce.save()
            print('Edit Announcement --', admin.user.username)
            return redirect('view_announcement')
    else:
        form = AnnouncementForm(instance=announcement)
    
    context = {
        'form': form,
        'title': 'Edit Anouncement'
    }

    return render(request, 'announcement/add_announcement.html', context=context)
    

@permission_required('announcement.delete_announcement')
def deleteAnnounce(request, announcement_id):
    announcement = AnnouncementModel.objects.get(pk=announcement_id)
    announcement.is_active = False
    announcement.save()
    print('Deleted --', announcement.id)
    return redirect('view_announcement')