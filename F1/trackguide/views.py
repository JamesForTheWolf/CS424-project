from django.shortcuts import render

from trackguide.models import Track
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from trackguide.forms import TrackForm

@login_required
def track_update(request,track_id):
    track = Track.objects.get(id=track_id)
    if request.method == "POST":
        form =TrackForm(request.POST,instance=track)
        if form.is_valid():
            form.save()
            return HttpResponse('Updated')
        else:
            return HttpResponse('Invalid data')
    form = TrackForm()
    return render(request,'trackguide/track_update.html',{
        'form':form
        })

def track(request,track_id):

    track = Track.objects.get(id=track_id)



    response = render(request,'trackguide/track_detail.html',{
        'track':track
    })

    return response



def tracks(request):

    tracks = Track.objects.all()



    response=render(request,'trackguide/track_list.html',{

            'tracks':tracks

    })

    return response